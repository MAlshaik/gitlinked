import supabase from "../../supabaseClient";
import { NextResponse } from "next/server";
export async function GET(req) {
    // Check if the method is GET
    /*
    if (req.method !== 'GET') {
        return res.status(405).send({ error: 'Method not allowed' });
    }
    */

    const { data, error } = await supabase
        .from('users_descriptive')
        .select('*');

    if (error) {
        console.error('Error fetching user data:', error);
        return NextResponse.json({ error: error.message });
    }

    return NextResponse.json(data);
  }