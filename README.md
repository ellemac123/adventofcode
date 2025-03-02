# adventofcode
Advent of Code Challenges in Python

Running through some of the Advent of Code challenges for each year I've missed. 
For reference: https://adventofcode.com/

## AoC Challenge in Python

### 2020, 2021, 2022, 2023, and 2024
I'm working through years 2020, 2021, 2022, 2023, and 2024 so far but plan to expand out as I get more time

Each of the files are python scripts, so you can run them in the usual way, but you need to 
`cd` into their directory as each has a corresponding puzzle input file.

All code is runnable via the command line, using Python 3. There are no extra libraries that need to be installed at this time.

eg: for `adventofcode/2024/day_ten/hoof_it.py`
```bash
cd adventofcode/2024/day_ten/
python hoof_it.py
```

## AoC Challenge in TypeScript

### 2019
I'll be working through the 2019 challenges to try and teach myself TypeScript. I'll do each problem in Python and Typescript. 

### Installation and Setup
I'll be using Deno to run each file. 

Install Node.js (and alongwith it NPM) here: https://nodejs.org/en/download/

Install typescript
```bash
npm install -g typescript
```

Install [Deno](https://docs.deno.com/runtime/) for runtime through CLI:
```bash
curl -fsSL https://deno.land/install.sh | sh
```

### Running Files with Deno

Pass in the `allow-read` flag when reading with Deno, as it will need permission to access the local files. 

```bash
deno --allow-read day_one.ts
```