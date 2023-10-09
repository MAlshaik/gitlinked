import supabase from "../../app/supabaseClient";

export default async function updateUserSearchHist(req, res) {
    // First, ensure the request method is appropriate
    if (req.method !== 'POST') {
      return res.status(405).json({ error: 'Method not allowed' });
    }

    const { userId, newSearch } = req.body;

    // Ensure the required fields are provided
    if (!userId || !newSearch) {
        return res.status(400).json({ error: 'Missing required fields.' });
    }

    try {
        const { data, error } = await supabase
          .from('users')
          .update({ searchhist: supabase.raw(`array_append(searchhist, ?)`, [newSearch]) })
          .eq('user_id', userId);
      
        if (error) {
          throw error;
        }
      
        return res.status(200).json({ success: true, message: 'Search history updated successfully', data });

    } catch (error) {
        console.error('Error updating search history:', error.message || error);
        return res.status(500).json({ error: 'Failed to update search history', details: error.message || error });
    }
}
