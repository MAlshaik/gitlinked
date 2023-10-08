import supabase from "../supabaseClient";

export default async function addUser(req, res) {
    
    if (req.method !== 'POST') {
      return res.status(405).send({ error: 'Method not allowed' });
    }
    
    const { data, error } = await supabase
      .from('contributors')
      .insert([
        {id: req.body.id, repos:req.body.repos, username:req.body.username},
      ]);
  
    if (error) {
      console.error('Error inserting user:', error);
      return res.status(500).send({ error: 'Error inserting user' });
    }
  
    return res.status(200).json({ success: true });
    
}
