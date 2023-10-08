import supabase from "../supabaseClient";

export default async function getRepo(req, res) {
  
  // Check if the method is POST
  if (req.method !== 'POST') {
    return res.status(405).send({ error: 'Method not allowed' });
  }

  const { data, error } = await supabase
    .from('repo')
    .select('*')
    .eq('repo_name', req.body.repo_name);

  if (error) {
    console.error('Error fetching repo:', error);
    return res.status(500).json({ error: error.message });
  }

  return res.status(200).json(data);
}
