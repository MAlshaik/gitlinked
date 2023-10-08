import { NextResponse } from "next/server";
export function GET(req) {
    // Check the request method
    NextResponse.json({ text: 'Hello from Imagine and AI Club, cool kids from MSU' });
}