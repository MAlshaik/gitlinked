import NextAuth from "next-auth";
import Github from "next-auth/providers/github";
import GitHubProvider from "next-auth/providers/github";

export default (req, res) =>
    NextAuth(req, res, {
        providers: [
            GitHubProvider({
                clientId: process.env.GITHUB_CLIENT_ID,
                clientSecret: process.env.GITHUB_CLIENT_SECRET,
            }),
        ],
        debug: process.env.NODE_ENV === "development",
        secret: process.env.AUTH_SECRET,
        jwt: {
            secret: process.env.JWT_SECRET,
        },
        callbacks: {
            async redirect(url, baseUrl) {
                return "/";
            },
        },
    });