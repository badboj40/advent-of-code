#  9   00:13:21   863      0   02:28:43  6965      0

from aocd.models import Puzzle
import time


def parse_indata():
    indata = [int(c) for c in Puzzle(2024, 9).input_data]
    fs = []   # (position, length, id)
    gaps = [] # (position, length)
    current_position = 0
    for i, length in enumerate(indata):
        if i % 2 and length > 0:
            gaps.append((current_position, length))
        if i % 2 == 0:
            fs.append((current_position, length, i//2))
        current_position += length
    return fs, gaps


def solve(part2=False):
    file_system, gaps = parse_indata()
    fixed_file_system = [] 

    for file_pos, file_length, id in reversed(file_system):
        minimum_gap_size = file_length if part2 else 1
        available_gaps = sorted([(p, l) for p,l in gaps if l >= minimum_gap_size and p < file_pos], reverse=True)

        while available_gaps and file_length > 0:
            gap_pos, gap_length = gap = available_gaps.pop()
            
            gaps.remove(gap)
            if gap_length > file_length:
                gaps.append((gap_pos + file_length, gap_length - file_length))

            fixed_file_system.append((gap_pos, min(file_length, gap_length), id))
            file_length -= gap_length
        
        if not available_gaps:
            fixed_file_system.append((file_pos, file_length, id))

    return sum(id * (p + i) for p, l, id in fixed_file_system for i in range(l))


if __name__ == "__main__":
    t0 = time.time()
    print("\npart1:", solve(part2=False))
    print("\npart2:", solve(part2=True))
    print("\ntime:", time.time()-t0)