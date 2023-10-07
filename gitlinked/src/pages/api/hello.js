export default function handler(req, res) {
    // Check the request method
    if (req.method === 'GET') {
        res.status(200).json({ text: 'Hello Next.js' });
    } else {
        res.status(405).end(); // Method Not Allowed
    }
}