import { NavLink, useLocation } from 'react-router-dom';
import classNames from 'classnames';
import { MenuData } from './MenuData';

function NavMenu() {
  const location = useLocation();
  const activeUrl = location.pathname;

  return (
    <>
      {MenuData.map(({ id, title, url, className }) => {
        const linkClasses = classNames(className, {
          active: activeUrl === url,
        });

        return (
          <li key={id} className="nav-item">
            <NavLink to={url} className={linkClasses}>
              {title}
            </NavLink>
          </li>
        );
      })}
    </>
  );
}

export default NavMenu;
