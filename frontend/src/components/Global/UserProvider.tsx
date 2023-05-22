import { createContext, useState, useEffect } from 'react';

interface UserContextValue {
  username: string | null;
  setUsername: React.Dispatch<React.SetStateAction<string | null>>;
  uploadedFiles: File[]; // Updated to an array of files
  setUploadedFiles: React.Dispatch<React.SetStateAction<File[]>>;
  currentFile: File | null; // Add currentFile
  setCurrentFile: React.Dispatch<React.SetStateAction<File | null>>; // Add setCurrentFile
}

interface UserProviderProps {
  children: React.ReactNode;
}

export const UserContext = createContext<UserContextValue | null>(null);

export const UserProvider = ({ children }: UserProviderProps) => {
  const [username, setUsername] = useState<string | null>(
    sessionStorage.getItem('username')
  );
  const [uploadedFiles, setUploadedFiles] = useState<File[]>([]);
  const [currentFile, setCurrentFile] = useState<File | null>(null); // Initialize currentFile with null

  useEffect(() => {
    sessionStorage.setItem('username', username || '');
  }, [username]);

  return (
    <UserContext.Provider
      value={{ username, setUsername, uploadedFiles, setUploadedFiles, currentFile, setCurrentFile }} // Include currentFile and setCurrentFile
    >
      {children}
    </UserContext.Provider>
  );
};
