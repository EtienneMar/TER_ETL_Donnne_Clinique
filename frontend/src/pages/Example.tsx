import { useContext, useEffect } from 'react';
import { UserContext } from '../components/Global/UserProvider';
import { Hero } from '../components/Hero';
import {UploadedFiles,  /*Table,*/ Dropdown, FileColumns} from '../components/Example';

function Example() {
  const userContext = useContext(UserContext);
  if (!userContext) {
      throw new Error("useContext(UserContext) is null, did you forget a UserProvider?");
  }
  const { uploadedFiles } = userContext;
  const lastUploadedFile = uploadedFiles[uploadedFiles.length - 1]

/*
              <FileColumns
                uploadedFileName={uploadedFileName}
                uploadedFile={uploadedFile}
              />
                            <Table />
*/
  return (
    <>
      <Hero title="Example Page 😁"
        content="  An About page is a special web page on a site where your
        readers/visitors learn more about you and what you do."
      ></Hero>
      <section className="py-5 bg-body-secondary">
        <div className="container py-5">
          <div className="row">
            <div className="col-lg-4">
              {lastUploadedFile && (
                <UploadedFiles
                  uploadedFile={lastUploadedFile}
                  uploadedFileName={lastUploadedFile.name}
                />
              )}
              <FileColumns
                uploadedFileName={lastUploadedFile.name}
              />
            </div>
            <div className="col-lg-6">

            </div>
            <div className="col-auto">
              <Dropdown />
            </div>
          </div>
        </div>
      </section>
    </>
  );
}

export default Example;