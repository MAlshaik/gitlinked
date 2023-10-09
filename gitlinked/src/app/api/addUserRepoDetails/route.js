import supabase from "../../supabaseClient";
import { NextApiRequest, NextApiResponse } from "next";
import { NextResponse } from "next/server";
import { NextRequest } from "next/server";

export async function POST(req) {
  const body = await req.json();

  console.log(body);
  console.log(body); 
  if (!body.exists) {
    const { data, error } = await supabase
      .from('users_descriptive')
      .insert([
        {
          id: body.id,
          repos: body.repos,
          interest: body.interest,
          availibility: body.availibility,
          skills: body.skills
        },
      ]);

    if (error) {
      console.error('Error inserting user:', error);
      return NextResponse.json({ error: error.message });
      
    }

    return NextResponse.json(data);
  } else {
    const { data, error } = await supabase
      .from('users_descriptive')
      .update([
        {
          id: body.id,
          repos: body.repos,
          interest: body.interest,
          availibility: body.availibility,
          skills: body.skills
        },
      ])
      .eq('id', body.id);

    if (error) {
      console.error('Error updating user:', error);
      return NextResponse.json({ error: error.message });
      
    }

    return NextResponse.json(data);
  }
}
