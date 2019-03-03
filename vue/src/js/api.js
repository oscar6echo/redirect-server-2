import axios from 'axios';

function requestServer(that, endpoint, callback) {
  const uri = `http://localhost:5000/${endpoint}`;

  const headers = {
    Accept: 'text/json'
  };

  const config = {
    method: 'get',
    url: uri,
    headers: headers
  };

  axios
    .request(config)
    .then(response => {
      callback(response.data);
    })
    .catch(error => {
      console.log('start error');
      console.log(error);
      console.log(error.response.data);
    });
}

export { requestServer };
