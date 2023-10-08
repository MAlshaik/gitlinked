import { NextResponse } from "next/server";
const { spawn } = require('child_process');
export async function POST(req) {
  const body = await req.json();
  /*
    if (req.method !== 'POST') {
      return res.status(405).json({ error: 'Method not allowed' });
    }
  */
    const pythonProcess = spawn('python', ['openai_script.py', '--prompt', body.prompt, '--id', body.id]);

    let pythonOutput = '';

    pythonProcess.stdout.on('data', (data) => {
        // Append data from Python script to pythonOutput variable
        pythonOutput += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        // Handle any errors
        console.error(`Python error: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        if (code !== 0) {
            console.log(`Python script exited with code ${code}`);
            return NextResponse.json({ error: `Python script exited with code ${code}`, pythonOutput: pythonOutput });
        } else {
            return NextResponse.json({ message: 'Script executed successfully', pythonOutput: pythonOutput });
        }
    });
  
  
  }
  