'use client'
import Image from 'next/image'
import Header from '@/components/header'
import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { NextRequest, NextResponse } from "next/server";
import { FormEvent } from 'react'
import Link from 'next/link';
import { useSession } from "next-auth/react"

export default function Home() {

  useEffect(() => {
    var head = document.getElementsByTagName("head")[0]
    head.getElementsByTagName("title")[0].innerHTML = "GitLinked"
  }, []);

  async function onSubmit(event) {
    event.preventDefault()
    const search = event.target[0]['value']


    

    if(search){
      push(`/main?prompt=${search}`)
    }

    
  }

  return (
      <>
      <Header />
      <main className="flex min-h-screen flex-col items-center justify-between p-[15rem] w-full">
        <form class="flex items-center w-[50%] min-w-[20rem]" onSubmit={onSubmit}>   
      <label for="simple-search" class="sr-only">Search</label>
      <div class="relative w-full">
          <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
              <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 20">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5v10M3 5a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm0 10a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm12 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm0 0V6a3 3 0 0 0-3-3H9m1.5-2-2 2 2 2"/>
              </svg>
          </div>
          <input method="POST" type="text" id="simple-search" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-3  dark:bg-purple-600 dark:border-gray-700 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="I am a beginner web developer and want to build a dating app for coders..." required/>
      </div>
      <button type="submit" class="p-2.5 ml-2 text-sm font-medium text-white bg-blue-700 rounded-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-purple-600 dark:hover:bg-purple-400 dark:focus:ring-blue-800">
          <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
          </svg>
          {/* <span class="sr-only">Search
          </span> */}
      </button>
      </form>
      <p>
        Please remember to sign in first! -Creators
      </p>
      </main>

    </>

 )
}
