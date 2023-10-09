import supabase from "../supabaseClient";

export default async function updateInterest(req, res) {
    if (req.method !== 'POST') {
      return res.status(405).json({ error: 'Method not allowed' });
    }

    try {
        const { data, error } = await supabase
          .from('users_descriptive')
          .update({ interest: req.body.interest })
          .eq('id', req.body.id);
      
        if (error) {
          throw error;
        }
      
        return res.status(200).json({ success: true, message: 'Interest updated successfully', data });

    } catch (error) {
        console.error('Error updating interest:', error.message || error);
        return res.status(500).json({ error: 'Failed to update interest', details: error.message || error });
    }
}
