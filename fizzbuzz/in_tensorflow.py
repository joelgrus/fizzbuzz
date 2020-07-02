from typing import NamedTuple, Callable
import math

import torch
import typer
from torch.utils.data import DataLoader


def fizz_buzz_class(n: int) -> int:
    return [1, 3, 5, 15].index(math.gcd(n, 15))


class Instance(NamedTuple):
    n: int
    features: torch.Tensor
    label: int

    @staticmethod
    def create(n: int, featurize: Callable) -> 'Instance':
        return Instance(n, featurize(n), fizz_buzz_class(n))


def evaluate(model: torch.nn.Module, 
             data: list,
             verbose = False) -> int:
    num_correct = 0

    # Don't compute gradients when evaluating
    with torch.no_grad():
        for n, features, label in data:
            predicted = torch.argmax(model(features)).item()
            num_correct += predicted == label

            if verbose:
                check = "✓" if predicted == label else "×"
                outputs = [str(n), 'fizz', 'buzz', 'fizzbuzz']
                print(check, n, outputs[predicted], outputs[label])

    return num_correct


def binary_digits(n: int, num_digits: int = 10) -> torch.Tensor:
    digits = []
    for _ in range(num_digits):
        # Need to use floats
        digits.append(float(n % 2))
        n = n // 2
    return torch.tensor(digits)


training_data = [Instance.create(n, binary_digits)
                 for n in range(101, 1023)]

test_data = [Instance.create(n, binary_digits)
             for n in range(1, 101)]

input_dim = len(training_data[0].features)


def train_model(
    hidden_dim: int = 25,
    num_epochs: int = 2500,
    seed: int = 12,
    output_path: str = None
) -> torch.nn.Module:
    torch.manual_seed(seed)

    model = torch.nn.Sequential(
        # Linear layer: input_dim -> hidden_dim
        torch.nn.Linear(in_features=input_dim, out_features=hidden_dim),
        # ReLU(x) = max(x, 0)
        torch.nn.ReLU(),
        # Linear layer: hidden_dim -> 4
        torch.nn.Linear(in_features=hidden_dim, out_features=4)
    )

    loss = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.AdamW(model.parameters())

    for epoch in range(num_epochs):
        epoch_loss = 0.0

        for batch in DataLoader(training_data, 
                                batch_size=5, 
                                shuffle=True):
            optimizer.zero_grad()

            predictions = model(batch.features)
            error = loss(predictions, batch.label)
            error.backward()
            epoch_loss += error.item()
            optimizer.step()

        num_correct = evaluate(model, 
                               test_data, 
                               verbose=epoch % 100 == 0)
        print(f"epoch: {epoch:>5} "
            f"accuracy: {num_correct}/100 "
            f"loss: {epoch_loss:.2f}")

    evaluate(model, test_data, verbose=True)

    return model

if __name__ == "__main__":
    typer.run(train_model)
