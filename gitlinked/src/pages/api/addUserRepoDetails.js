import supabase from "../supabaseClient";

export default async function addUserRepoDetails(req, res) {
  if (!req.body.exists) {
    const { data, error } = await supabase
      .from('users_descriptive')
      .insert([
        {
          id: req.body.id,
          repos: req.body.repos,
          interest: req.body.interest,
          availibility: req.body.availibility,
          skills: req.body.skills
        },
      ]);

    if (error) {
      console.error('Error inserting user:', error);
      res.status(500).json({ error: error.message });
      return;
    }

    return res.status(200).json(data);
  } else {
    const { data, error } = await supabase
      .from('users_descriptive')
      .update([
        {
          id: req.body.id,
          repos: req.body.repos,
          interest: req.body.interest,
          availibility: req.body.availibility,
          skills: req.body.skills
        },
      ])
      .eq('id', req.body.id);

    if (error) {
      console.error('Error updating user:', error);
      res.status(500).json({ error: error.message });
      return;
    }

    return res.status(200).json(data);
  }
}
