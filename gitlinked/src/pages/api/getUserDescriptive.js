import supabase from "../../supabaseClient";

export default async function getUserDescriptive(req, res) {
  
  // Check if the method is POST
  if (req.method !== 'POST') {
    return res.status(405).send({ error: 'Method not allowed' });
  }

  const { data, error } = await supabase
    .from('users_descriptive')
    .select('*')
    .eq('id', req.body.id)
    .single();

  if (error) {
    console.error('Error fetching user:', error);
    return res.status(500).json({ error: error.message });
  }

  return res.status(200).json(data);
}
