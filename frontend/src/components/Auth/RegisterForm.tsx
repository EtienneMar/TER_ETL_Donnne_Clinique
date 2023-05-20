import { BsPersonCircle, BsEnvelope, BsLock, BsKey, BsBoxArrowUpRight } from 'react-icons/bs';
import { FormEvent } from 'react';

function RegisterForm() {
  
  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const form = event.target as HTMLFormElement;
    const formData = new FormData(form);
    const username = formData.get('username') as string;
    const email = formData.get('email') as string;
    const password = formData.get('password') as string;

    try {
      const response = await fetch('http://localhost:5005/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username,
          email,
          password,
        }),
      });

      if (response.ok) {
        const data = await response.json();
        console.log(data);
        // TODO: Handle response data, e.g., show a success message, redirect, etc.
      } else {
        throw new Error('An error occurred');
      }
    } catch (error) {
      console.log('An error occurred:', error);
      // TODO: Handle error, e.g., show an error message, clear form fields, etc.
    }
  };


  return (
    <form className="card" onSubmit={handleSubmit}>
      <div className="card-header bg-transparent py-3">
        <h4 className="text-capitalize text-center fw-semibold mb-0">
          Register
        </h4>
      </div>
      <div className="card-body">
        <div className="input-group mb-3">
          <span id="name-addon" className="input-group-text">
            <BsPersonCircle size="20" />
          </span>
          <input
            type="text"
            className="form-control"
            placeholder="Name"
            aria-label="Name"
            aria-describedby="name-addon"
            required
            name='username'
          />
        </div>
        <div className="input-group mb-3">
          <span id="email-addon" className="input-group-text">
            <BsEnvelope size="20" />
          </span>
          <input
            type="email"
            className="form-control"
            placeholder="Email"
            aria-label="Email"
            aria-describedby="email-addon"
            required
            name='email'
          />
        </div>
        <div className="input-group mb-3">
          <span id="password-addon" className="input-group-text">
            <BsLock size="20" />
          </span>
          <input
            type="password"
            className="form-control"
            placeholder="Password"
            aria-label="Password"
            aria-describedby="password-addon"
            required
          />
        </div>
        <div className="input-group mb-3">
          <span id="confirm-password-addon" className="input-group-text">
            <BsKey size="20" />
          </span>
          <input
            type="password"
            className="form-control"
            placeholder="Confirm Password"
            aria-label="Confirm Password"
            aria-describedby="confirm-password-addon"
            required
            name='password'
          />
        </div>
        <div className="form-check mb-0">
          <input
            type="checkbox"
            id="terms-agreement"
            className="form-check-input"
            defaultValue=""
            defaultChecked
          />
          <label className="form-check-label" htmlFor="terms-agreement">
            I agree all statements in Terms of service
          </label>
        </div>
      </div>
      <div className="card-footer bg-transparent py-3">
        <button
          type="submit"
          className="btn btn-primary d-inline-flex align-items-center justify-content-center gap-2 w-100"
        >
          <span className="text-capitalize">Register Now</span>
          <BsBoxArrowUpRight size="20" />
        </button>
      </div>
    </form>
  );
}

export default RegisterForm;
