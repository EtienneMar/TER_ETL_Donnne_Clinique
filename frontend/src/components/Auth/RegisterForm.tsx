import {
  BsPersonCircle,
  BsEnvelope,
  BsLock,
  BsKey,
  BsBoxArrowUpRight,
} from 'react-icons/bs';

function RegisterForm() {
  return (
    <form className="card">
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
