import supabase from "../../supabaseClient";
import { NextResponse } from "next/server";
export async function POST(req) {
  const body = await req.json();
  /*
    if (req.method !== 'POST') {
      return res.status(405).json({ error: 'Method not allowed' });
    }
*/
    try {
        const { data, error } = await supabase
          .from('users_descriptive')
          .update({ availibility :  body.availibility })
          .eq('id', body.id);
      
        if (error) {
          throw error;
        }
      
        return NextResponse.json({ success: true, message: 'Availability updated successfully', data });

    } catch (error) {
        console.error('Error updating weekly availability:', error.message || error);
        return NextResponse.json({ error: 'Failed to update availability', details: error.message || error });
    }
}
