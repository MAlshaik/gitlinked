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
    .from('repo')
    .select('*')
    .eq('repo_name', body.repo_name);

  if (error) {
    console.error('Error fetching repo:', error);
    return NextResponse.json({ error: error.message });
  }

  return NextResponse.json(data);
}
