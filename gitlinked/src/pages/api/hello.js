export default function handler(req, res) {
    // Check the request method
    if (req.method === 'GET') {
        res.status(200).json({ text: 'Hello from Imagine and AI Club, cool kids from MSU' });
    } else {
        res.status(405).end(); // Method Not Allowed
    }
}