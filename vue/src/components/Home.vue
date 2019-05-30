<template>
  <div id="my-wrapper">
    <div id="my-navbar" class="d-flex flex-column align-items-center">
      <div class="d-flex justify-content-center align-items-center">
        <img id="logo" src="../assets/compass.png" />
        <div id="my-title">Redirect Server</div>
      </div>
      <div id="my-subtitle">To help keep your links tidy and short</div>
    </div>

    <b-container class="mt-3">
      <div class="d-flex flex-column align-items-center">
        <div>
          <h3 id="my-section-head">User Guide</h3>
          The table below contains the list
          <strong>redirect rules</strong> by decreasing order of precedence.
          <br />Each line contains:
          <ul>
            <li>
              A
              <a href="https://www.regular-expressions.info/">regex</a>
              to match short urls
            </li>
            <li>
              A route i.e. a corresponding
              <a
                href="https://www.regular-expressions.info/replacetutorial.html"
                >replacement string</a
              >
            </li>
            <li>A source file from where the rule is read</li>
          </ul>
          The priority is set:
          <ul>
            <li>by order of source files</li>
            <li>then by order of entries in each source file</li>
          </ul>
          The redirects are extracted from the following files:
          <ul>
            <li v-for="(item, index) in redirectSources" :key="index">
              <a :href="item">{{ item }}</a>
            </li>
          </ul>
          To update the redirect rules - updated every
          {{ updatePeriod }} seconds:
          <ul>
            <li>add an entry to a source file</li>
            <li>
              or request the addition of a new source file to the administrator
            </li>
          </ul>
          <b-card
            border-variant="success"
            text-variant="success"
            style="width: 32rem"
          >
            <b-card-text>
              <strong>Advice:</strong> Test your regex and replacement strings
              in
              <a href="https://regex101.com/">regex101.com</a>
            </b-card-text>
          </b-card>
          <h3 id="my-section-head">Redirect Rules Table</h3>
          <b-table bordered :items="rulesStatus" id="status-status" />
          <b-table striped hover small :items="redirectRules" />
          <h3 id="my-section-head">Test Zone</h3>

          Test a short url against the redirect rules in table above
          <b-row>
            <b-col cols="8">
              <b-input-group prepend="Short Url" class="mt-3">
                <b-form-input v-model="testShortUrl" />
                <b-input-group-append>
                  <b-button variant="primary" @click="getRedirectUrl()"
                    >Test</b-button
                  >
                </b-input-group-append>
              </b-input-group>
            </b-col>
          </b-row>

          <b-row>
            <b-col cols="8">
              <b-card border-variant="primary" id="test-result">
                <b-card-text>
                  <a :href="testRedirectUrl">{{ testRedirectUrl }}</a>
                </b-card-text>
              </b-card>
            </b-col>
          </b-row>
        </div>
      </div>
    </b-container>
  </div>
</template>

<script>
import { requestServer } from '../js/api';

export default {
  name: 'Home',
  data() {
    return {
      redirectRules: [],
      interval: null,
      updatePeriod: 0,
      startTime: '',
      updateTime: '',
      testShortUrl: '',
      testRedirectUrl: 'No matching url'
    };
  },
  beforeMount() {
    // admin
    const callbackAdmin = this.setAdmin;
    requestServer(this, 'redirect-server-admin', callbackAdmin);

    // redirectRules
    const callbackRules = this.setRedirectRules;
    requestServer(this, 'redirect-rules', callbackRules);
    this.interval = setInterval(
      () => requestServer(this, 'redirect-rules', callbackRules),
      1000 * 30
    );
  },
  methods: {
    setAdmin: function(data) {
      this.updatePeriod = data.updatePeriod;
      this.startTime = data.startTime;
      console.log('admin data loaded');
    },
    setRedirectRules: function(data) {
      this.updateTime = data.updateTime;
      this.redirectRules = data.redirectRules;
      console.log('redirectRules updated');
    },
    getRedirectUrl: function() {
      const callbackTestUrl = this.setRedirectUrl;
      requestServer(
        this,
        'test-shorturl-' + this.testShortUrl,
        callbackTestUrl
      );
    },
    setRedirectUrl: function(data) {
      const ru = data.testRedirectUrl;
      this.testRedirectUrl = ru == '/info' ? 'No matching url' : ru;
      console.log('testRedirectUrl updated');
    }
  },
  computed: {
    redirectSources: function() {
      const sources = this.redirectRules.map(e => e.source);
      return [...new Set(sources)];
    },
    rulesStatus: function() {
      return [
        {
          'Server started': this.startTime,
          'Last Rules Update': this.updateTime
        }
      ];
    }
  }
};
</script>

<style lang="scss" scoped>
#my-wrapper {
  margin-bottom: 50px;
}
#my-navbar {
  padding: 10px;
  border-bottom: $border-light;
}
#logo {
  width: 35px;
  height: 35px;
}
#my-title {
  color: $title-color;
  font-size: 30px;
  margin-left: 10px;
}
#my-subtitle {
  margin: 10px 0 10px 0;
  font-size: 18px;
}
#my-section-head {
  margin: 15px;
  margin-top: 30px;
}
#status-status {
  width: 500px;
}
#test-button {
  width: 100px;
}
#test-result {
  margin-top: 10px;
  padding: 10px;
}
#test-result .card-body {
  padding: 0rem;
}
</style>
