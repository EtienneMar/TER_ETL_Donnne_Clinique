// UserContext.tsx
import { createContext, useState, useEffect } from 'react';

interface UserContextValue {
  username: string | null;
  setUsername: React.Dispatch<React.SetStateAction<string | null>>;
}

interface UserProviderProps {
    children: React.ReactNode;
  }
  

export const UserContext = createContext<UserContextValue | null>(null);

export const UserProvider = ({ children }: UserProviderProps) => {
  const [username, setUsername] = useState<string | null>(sessionStorage.getItem('username'));

  useEffect(() => {
    // Whenever the username state changes, update session storage
    sessionStorage.setItem('username', username || '');
  }, [username]);

  return (
    <UserContext.Provider value={{ username, setUsername }}>
      {children}
    </UserContext.Provider>
  );
};
