import supabase from "../supabaseClient";

export default async function updateAvailibility(req, res) {
    if (req.method !== 'POST') {
      return res.status(405).json({ error: 'Method not allowed' });
    }

    try {
        const { data, error } = await supabase
          .from('users_descriptive')
          .update({ availibility :  req.body.availibility })
          .eq('id', req.body.id);
      
        if (error) {
          throw error;
        }
      
        return res.status(200).json({ success: true, message: 'Availability updated successfully', data });

    } catch (error) {
        console.error('Error updating weekly availability:', error.message || error);
        return res.status(500).json({ error: 'Failed to update availability', details: error.message || error });
    }
}
