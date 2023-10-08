import supabase from "../supabaseClient";
const { spawn } = require('child_process');

export default function updateUserDetails(req, res) {
    const userId = req.body.userId;
    const username = req.body.username;

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
            return res.status(500).json({ error: `Python script exited with code ${code}`, details: scriptOutput });
        }
        return res.status(200).json({ message: "Script executed successfully", data: scriptOutput });
    });
}
