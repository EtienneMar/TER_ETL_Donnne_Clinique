import { Link } from 'react-router-dom';
import NavMenu from './NavMenu';
import { BsFillPersonPlusFill, BsShieldLockFill } from 'react-icons/bs';
import { useContext } from 'react';
import { UserContext } from '../Global/UserProvider'

function Header() {


  const userContext = useContext(UserContext);
  if (!userContext) {
    throw new Error("useContext(UserContext) is null, did you forget a UserProvider?");
  }
  const { username } = userContext;

  return (
    <nav className="navbar navbar-expand-lg bg-body-secondary py-3 sticky-top">

      <div className="container">

        <Link to="/" className="navbar-brand">Icops</Link> 

        <button type="button"  className="navbar-toggler" data-bs-toggle="collapse" 
                data-bs-target="#navbarNav" aria-controls="navbarNav"
                aria-expanded="false" aria-label="Toggle Navigation">
          <span className="navbar-toggler-icon" />
        </button>
        
        <div id="navbarNav" className="navbar-collapse collapse">
          
          <ul className="navbar-nav my-lg-0 my-2">
            <NavMenu />
          </ul>
          <div className="d-grid d-lg-flex gap-2 ms-lg-auto">
              {username ? (
              <div className="m-2 bg-white text-black">
                <h5 className=" text-capitalize">{username}</h5>
              </div>
              ) : (
                <>
                  <Link to="/register" className="btn btn-primary d-inline-flex align-items-center justify-content-center gap-2">
                    <BsFillPersonPlusFill size="20" />
                    <span className="text-capitalize">Register</span>
                  </Link>
                  <Link to="/login" className="btn btn-dark d-inline-flex align-items-center justify-content-center gap-2">
                    <BsShieldLockFill size="20" />
                    <span className="text-capitalize">Login</span>
                  </Link>
                </>
              )}
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Header;