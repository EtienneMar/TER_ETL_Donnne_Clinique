interface HeroProps {
  title: string;
  content: string;
}

function Hero({title, content}: HeroProps) {
  return (
    <section className="py-5 bg-body-tertiary">
      <div className="container py-5 text-center">
        <h1 className="display-5 text-primary fw-bold">{title}</h1>
        <div className="col-lg-7 mx-auto">
          <p className="lead mb-0"> {content}</p>
        </div>
      </div>
    </section>
  );
}

export default Hero;
