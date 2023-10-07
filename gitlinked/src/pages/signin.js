import { signIn, useSession } from 'next-auth/react';

export default function SignIn() {
  const { data: session } = useSession();

  if (session) {
    console.log(session);
    return (
      <div>
        You are already signed in! <a href="/">Go back to home.</a>
      </div>
    );
  }

  return (
    <div>
      <h2>Sign In</h2>
      <button onClick={() => signIn('github')}>Sign in with GitHub</button>
      {/* Add other providers or a custom form as needed */}
    </div>
  );
}
