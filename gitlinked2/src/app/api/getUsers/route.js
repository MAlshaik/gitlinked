import supabase from "../../supabaseClient";
import { NextResponse } from "next/server";
export async function GET(req) {
  const body = await req.json();

  // Check if the method is GET
  /*
  if (req.method !== 'GET') {
    return res.status(405).send({ error: 'Method not allowed' });
  }
  */

  const { data, error } = await supabase
    .from('users')
    .select('*');

  if (error) {
    console.error('Error fetching users:', error);
    return NextResponse.json({ error: error.message });
  }

  //return json({'message' : 'works'});
  return NextResponse.json({ message: 'Internal server error' })
}

// export const handler = getUsers();
//export {handler as GET};