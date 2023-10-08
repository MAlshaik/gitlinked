import supabase from "../supabaseClient";

export default async function addRepo(req, res) {
    
    if (req.method !== 'POST') {
      return res.status(405).send({ error: 'Method not allowed' });
    }

    const { data, error } = await supabase
      .from('repo')
      .insert([
        {
          repo_name: req.body.repo_name,
          top_contributors: req.body.top_contributors,
          description: req.body.description,
          README: req.body.README,
          Languages: req.body.languages
        },
      ]);

    if (error) {
      console.error('Error inserting repo:', error);
      return res.status(500).send({ error: 'Error inserting repo' });
    }

    return res.status(200).json({ success: true });
}
