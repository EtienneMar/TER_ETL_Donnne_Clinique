import { Routes, Route } from 'react-router-dom';
import { Header, Footer } from './components';
import { Home, About, Register, Mapping, Login, NotFound, } from './pages';
import { UserProvider } from './components/Global/UserProvider'

function App() {
  return (
    <>
      <UserProvider>
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/mapping" element={<Mapping />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
        <Footer />
      </UserProvider>
    </>
  );
}

export default App;
