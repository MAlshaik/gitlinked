import NextAuth from "next-auth"
import GithubProvider from "next-auth/providers/github"

export const authOptions = {
  // Configure one or more authentication providers
  providers: [
    GithubProvider({
      clientId: process.env.GITHUB_ID,
      clientSecret: process.env.GITHUB_SECRET,
      redirectUri: process.env.GITHUB_REDIRECT_URI,
    }),
  ],
    secret: process.env.AUTH_SECRET,
}

export const handler = NextAuth(authOptions);

export {handler as GET, handler as POST};
