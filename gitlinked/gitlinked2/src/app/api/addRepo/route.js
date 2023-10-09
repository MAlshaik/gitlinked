import supabase from "../../supabaseClient";
import { NextResponse } from "next/server";

export async function POST(req) {
    const body = await req.json()

    /*
    if (req.method !== 'POST') {
      return NextResponse.send({ error: 'Method not allowed' });
    }
    */

    const { data, error } = await supabase
      .from('repo')
      .insert([
        {
          repo_name: body.repo_name,
          top_contributors: body.top_contributors,
          description: body.description,
          README: body.README,
          Languages: body.languages
        },
      ]);

    if (error) {
      console.error('Error inserting repo:', error);
      return NextResponse.send({ error: 'Error inserting repo' });
    }

    return NextResponse.json({ success: true });
}
