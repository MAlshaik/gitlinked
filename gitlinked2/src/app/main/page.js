'use client';

import Image from 'next/image';
import Script from "next/script";
import { useEffect } from 'react';
import Header from '@/components/header'
import Accordion from '@/components/accordion';
import Drawer from '@/components/drawer';


export default function Home() {
    useEffect(() => {
        const users = [
            {
              id: 1,
              name: "Tatiana Pavlova",
              username: "tatiana_pavlova",
              image_url:
                "https://images.unsplash.com/photo-1626071466175-79ab723e9fdd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=759&q=80",
            },
            {
              id: 2,
              name: "Aiony Haust",
              username: "aiony_haust",
              image_url:
                "https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80",
            },
            {
              id: 3,
              name: "Joel Mott",
              username: "joel_mott",
              image_url:
                "https://images.unsplash.com/photo-1548142813-c348350df52b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=689&q=80",
            },
            {
              id: 4,
              name: "Caique Silva",
              username: "caique_silva",
              image_url:
                "https://images.unsplash.com/photo-1504363081893-c8226db66926?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
            },
            {
              id: 5,
              name: "Jemima Wood",
              username: "jemima_wood",
              image_url:
                "https://images.unsplash.com/photo-1644456070980-a6be4db8910a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
            },
            {
              id: 6,
              name: "Leio McLaren",
              username: "leio_mclaren",
              image_url:
                "https://images.unsplash.com/photo-1628157588553-5eeea00af15c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80",
            },
            {
              id: 7,
              name: "Alex Suprun",
              username: "alex_suprun",
              image_url:
                "https://images.unsplash.com/photo-1640951613773-54706e06851d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80",
            },
            {
              id: 8,
              name: "Charles Deluvio",
              username: "charles_deluvio",
              image_url:
                "https://images.unsplash.com/photo-1543610892-0b1f7e6d8ac1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
            },
            {
              id: 9,
              name: "Luis Villasmil",
              username: "luis_villasmil",
              image_url:
                "https://images.unsplash.com/photo-1624561172888-ac93c696e10c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDN8fGF2YXRhcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60",
            },
            {
              id: 10,
              name: "Jabari Timothy",
              username: "jabari_timothy",
              image_url:
                "https://images.unsplash.com/photo-1656473040206-53753fbbc767?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
            },
            {
              id: 11,
              name: "Ben Parker",
              username: "ben_parker",
              image_url:
                "https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
            },
            {
              id: 12,
              name: "Ayo Ogunseinde",
              username: "ayo_ogunseinde",
              image_url:
                "https://images.unsplash.com/photo-1463453091185-61582044d556?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
            },
            {
              id: 13,
              name: "Vince Fleming",
              username: "vince_fleming",
              image_url:
                "https://images.unsplash.com/photo-1522556189639-b150ed9c4330?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
            },
            {
              id: 14,
              name: "Huston Wilson",
              username: "huston_wilson",
              image_url:
                "https://images.unsplash.com/photo-1507114845806-0347f6150324?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
            },
            {
              id: 15,
              name: "Leon Ell'",
              username: "leon_ell",
              image_url:
                "https://images.unsplash.com/photo-1523824921871-d6f1a15151f1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
            },
          ];
          
          const storiesContainer = document.querySelector(".stories");
          users.map((user) => {
            storiesContainer.innerHTML += `
            <li class="flex flex-none flex-col items-center space-y-1 user">
            <div
              class="bg-gradient-to-tr from-yellow-400 to-fuchsia-600 p-1 rounded-full"
            >
              <a href="#" class="block bg-white p-1 rounded-full relative">
                <img
                  src="${user.image_url}"
                  alt="${user.name}"
                  class="w-16 h-16 rounded-full object-cover"
                />
              </a>
            </div>
            <a href="#" class="text-xs text-slate-800"
              >${user.username}</a
            >
          </li>
            `;
          });
    }, []);

    useEffect(() => {

        const drawer = document.getElementById("drawer-contact");
        const close = document.getElementById("close");
        const users = document.querySelectorAll(".user");

        console.log(users)

        users.forEach(element => {
            element.addEventListener("click", () => {
              drawer.classList.remove("-translate-x-full");
              drawer.classList.add("-translate-x-0");
            });
        });

        close.addEventListener("click", () => {
            drawer.classList.add("-translate-x-full");
            drawer.classList.remove("-translate-x-0");
            console.log(drawer.classList)
          }
        );
      }, []);

    return (
        <>
        <Header />
       <section class="bg-black-800 w-screen flex justify-center items-center">
      <ul
        class="w-full md:w-3/4 m-2 lg:w-1/2 flex justify-between items-start mb-8 space-x-3 overflow-x-scroll stories bg-white p-4 rounded drop-shadow-xl"
      >
      </ul>
    </section>
    <Accordion />
    <Drawer />
    </>
    )
}