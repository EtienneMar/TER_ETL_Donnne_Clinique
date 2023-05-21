import { createContext, useState, useEffect } from 'react';

interface UserContextValue {
  username: string | null;
  setUsername: React.Dispatch<React.SetStateAction<string | null>>;
  uploadedFiles: File[]; // Updated to an array of files
  setUploadedFiles: React.Dispatch<React.SetStateAction<File[]>>; // Updated to set an array of files
}

interface UserProviderProps {
  children: React.ReactNode;
}

export const UserContext = createContext<UserContextValue | null>(null);

export const UserProvider = ({ children }: UserProviderProps) => {
  const [username, setUsername] = useState<string | null>(
    sessionStorage.getItem('username')
  );
  const [uploadedFiles, setUploadedFiles] = useState<File[]>([]); // Updated to an array of files

  useEffect(() => {
    sessionStorage.setItem('username', username || '');
  }, [username]);

  return (
    <UserContext.Provider
      value={{ username, setUsername, uploadedFiles, setUploadedFiles }} // Updated to include uploadedFiles and setUploadedFiles
    >
      {children}
    </UserContext.Provider>
  );
};
