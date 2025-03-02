/*
The Typescript solution for: https://adventofcode.com/2019/day/1
The answer to part one is: 3311492
The answer to part one is: 4964376
*/ 
import * as fs from 'node:fs';

function readFileFunction(): Promise<string> {
    // read and return the input file text
    return new Promise((resolve, reject) => {
        fs.readFile('input.txt', 'utf-8', (err, data) => {
            if(err) {
                console.error('cannot read local file')
                reject('cannot read local file')
            }
            resolve(data)
        });
    }
)}


function calculateEquation(listVelocities: string[]): number[]{
    /*
    Given a list of numbers, calculate the fuel required by 
    dividing its value by three, rounding down, and 
    then subtracting 2
    */
    let totalFuelRequired = 0;
    let totalFuelRequiredPartTwo = 0

    listVelocities.forEach((velocity:string)=>{
        let tempVelocity: number = (velocity as unknown) as number;
        tempVelocity = Math.floor(tempVelocity / 3) - 2;
        totalFuelRequired += tempVelocity;

        while(tempVelocity>0){
            totalFuelRequiredPartTwo += tempVelocity; 
            tempVelocity = Math.floor(tempVelocity / 3) - 2;
        }
    });

    return [totalFuelRequired, totalFuelRequiredPartTwo];
}

async function main(): Promise<number[] | string> {
    /*
        Read the input file, and call associated functions to perfrom calculation for 
        the fuel required.
    */
    let fileData: string;

    try {
        fileData = await readFileFunction();
    } catch(err) {
        console.error('error reading file');
        return('error while trying to read file');
    }

    let velocities: Array<string> = fileData.split('\n');
    const totalFuelNeeded: Array<number> = calculateEquation(velocities);
    return totalFuelNeeded
    
}

// run code and print the result to screen
let result: string | number[] = await main();
console.log(`The answer to part one is: ${result[0]}`)
console.log(`The answer to part one is: ${result[1]}`)