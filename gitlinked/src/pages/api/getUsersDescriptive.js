import supabase from "../supabaseClient";
export default async function getUsersDescriptive(req, res) {
    // Check if the method is GET
    if (req.method !== 'GET') {
        return res.status(405).send({ error: 'Method not allowed' });
    }

    const { data, error } = await supabase
        .from('users_descriptive')
        .select('*');

    if (error) {
        console.error('Error fetching user data:', error);
        return res.status(500).json({ error: error.message });
    }

    return res.status(200).json(data);
  }