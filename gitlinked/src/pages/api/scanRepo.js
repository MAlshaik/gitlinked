const { spawn } = require('child_process');

export default async function scanRepo(req, res) {
    const pythonProcess = spawn('python', ['get_contributors.py', '--name', req.body.name]);

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
            return res.status(500).json({ error: `Python script exited with code ${code}`, pythonOutput: pythonOutput });
        } else {
            return res.status(200).json({ message: 'Script executed successfully', pythonOutput: pythonOutput });
        }
    });
}
