import fileinput
from collections import defaultdict
from functools import partial
from itertools import count, pairwise, starmap
from operator import eq, sub
from typing import NamedTuple, Self


def main():
    robots = list(map(Robot.parse, fileinput.input()))

    print(part_1(robots, 100, 101, 103))
    print(part_2(robots, 101, 103))


class Position(NamedTuple):
    x: int
    y: int


class Velocity(NamedTuple):
    x: int
    y: int


class Robot(NamedTuple):
    position: Position
    velocity: Velocity

    @classmethod
    def parse(cls, raw_robot: str) -> Self:
        raw_position, raw_velocity = raw_robot.split()
        position = Position(*map(int, raw_position.split('=')[1].split(',')))
        velocity = Velocity(*map(int, raw_velocity.split('=')[1].split(',')))

        return cls(position, velocity)

    def after(self, seconds: int, width: int, height: int) -> Self:
        return Robot(Position((self.position.x + self.velocity.x * seconds) % width,
                              (self.position.y + self.velocity.y * seconds) % height), self.velocity)


def part_1(robots: list[Robot], seconds: int, width: int, height: int) -> int:
    quadrants = [[0, 0],
                 [0, 0]]
    center_x = width // 2
    center_y = height // 2

    for robot in robots:
        robot = robot.after(seconds, width, height)

        if robot.position.x != center_x and robot.position.y != center_y:
            quadrants[robot.position.y > center_y][robot.position.x > center_x] += 1

    return quadrants[0][0] * quadrants[0][1] * quadrants[1][0] * quadrants[1][1]


def part_2(robots: list[Robot], width: int, height: int) -> int:
    positions = [list(robot.position) for robot in robots]

    for seconds in count():
        xs = defaultdict(set)

        for robot, position in zip(robots, positions):
            xs[position[1]].add(position[0])
            position[0] = (position[0] + robot.velocity.x) % width
            position[1] = (position[1] + robot.velocity.y) % height

        for xs in xs.values():
            if len(xs) >= 31 and sum(map(partial(eq, 1), starmap(sub, pairwise(sorted(xs, reverse=True))))) >= 30:
                return seconds


if __name__ == '__main__':
    main()
