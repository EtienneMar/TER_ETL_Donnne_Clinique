import { Hero } from '../components/Hero';
import { FileUpload } from '../components';
function Home() {
  return (
    <>
      <Hero 
      title="Home Page 😎"
      content="            A home page is the main web page of a website. The term may also
      refer to the start page shown in a web browser when the application
      first opens. Usually, the home page is located at the root of the
      website's domain or subdomain."
      />
      <FileUpload />
    </>
  );
}

export default Home;
