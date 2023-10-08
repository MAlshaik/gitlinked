import { NextResponse } from "next/server";
import supabase from "../../supabaseClient";

export async function POST(req) {
  const body = await req.json();

  // Check if the method is POST
  /*
  if (req.method !== 'POST') {
    return res.status(405).send({ error: 'Method not allowed' });
  }
  */

  const { data, error } = await supabase
    .from('users_descriptive')
    .select('*')
    .eq('id', body.id)
    .single();

  if (error) {
    console.error('Error fetching user:', error);
    return NextResponse.json({ error: error.message });
  }

  return NextResponse.json(data);
}
