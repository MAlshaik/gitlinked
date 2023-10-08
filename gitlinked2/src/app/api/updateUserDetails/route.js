import supabase from "../../supabaseClient";
const { spawn } = require('child_process');
import { NextResponse } from "next/server";
export async function POST(req, res) {
    const body = await req.json();

    const userId = body.userId;
    const username = body.username;

    const pythonProcess = spawn('python', ['get_info.py', '--id', userId, '--username', username, '--exists', true]);
                  
    let scriptOutput = "";

    pythonProcess.stdout.on('data', (data) => {
        // Collect data from the Python script
        scriptOutput += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        // Handle any errors
        console.error(`Python error: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        if (code !== 0) {
            console.error(`Python script exited with code ${code}`);
            return NextResponse.json({ error: `Python script exited with code ${code}`, details: scriptOutput });
        }
        return NextResponse.json({ message: "Script executed successfully", data: scriptOutput });
    });
}
