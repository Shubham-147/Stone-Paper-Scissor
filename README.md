# Rock–Paper–Scissors (Stone–Paper–Scissor)

A command-line game where you play one round of rock–paper–scissors against the computer.

## How to Run

```bash
python stonePaperScissor.py
```

## How to Play

1. When prompted, enter your choice as an integer.
2. The computer picks randomly from the same three options.
3. The program prints both choices and whether you **won**, **lost**, or **drew**.

## Choices

| Input | Move    |
|-------|---------|
| `-1`  | Scissor |
| `0`   | Stone   |
| `1`   | Paper   |

## Rules

| Outcome | Condition |
|---------|-----------|
| **Draw** | Both players choose the same move |
| **Win**  | Your move beats the computer's move |
| **Loss** | The computer's move beats yours |

Classic matchups:

- **Scissor** beats paper, loses to stone
- **Stone** beats scissor, loses to paper
- **Paper** beats stone, loses to scissor

## Example Output

```
Enter your Choice(
 1-> paper,
0->stone,
-1->paper
)
0
{-1: 'scissor', 0: 'stone', 1: 'paper'}
Your Choice stone, System Choice paper
You Lost
```

## Project Structure

| File | Description |
|------|-------------|
| `stonePaperScissor.py` | Main game script |
| `stonePaperScissor.md` | This documentation |

## Notes

- Each run plays **one round** only.
- The program prints the full choice dictionary before showing the result.
- The input prompt labels `-1` as "paper" in the message, but the code maps `-1` to **scissor**. Use the table above when playing.
