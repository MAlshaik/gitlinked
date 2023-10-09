import supabase from "../../supabaseClient";
import { NextResponse } from "next/server";

export async function POST(req, res) {
  const body = await req.json();
  // Check if the method is POST
  /*
  if (req.method !== 'POST') {
    return res.status(405).send({ error: 'Method not allowed' });
  }
  */

  const { data, error } = await supabase
    .from('users')
    .select('*')
    .eq('id', body.id)
    .single();

  if (error) {
    console.error('Error fetching user:', error);
    return NextResponse.json({ error: error.message });
  }

  return NextResponse.json(data);
}
