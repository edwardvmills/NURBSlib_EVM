



<!DOCTYPE html>
<html lang="en" class=" is-copy-enabled">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=1020">
    <meta content="origin-when-cross-origin" name="referrer" />
    
    <title>NURBSlib_EVM/README.md at master · edwardvmills/NURBSlib_EVM</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="edwardvmills/NURBSlib_EVM" name="twitter:title" /><meta content="NURBSlib_EVM - My python scripts for FreeCAD" name="twitter:description" /><meta content="https://avatars1.githubusercontent.com/u/11814550?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars1.githubusercontent.com/u/11814550?v=3&amp;s=400" property="og:image" /><meta content="edwardvmills/NURBSlib_EVM" property="og:title" /><meta content="https://github.com/edwardvmills/NURBSlib_EVM" property="og:url" /><meta content="NURBSlib_EVM - My python scripts for FreeCAD" property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/MTE4MTQ1NTA6ZDRmZDBiNjhkYThkYmJlMTQzZjY5M2E2MDMwOTMyMDY6Y2FjMmJkMzlmYmZhMmVmNzg5ZDcwZTE3ZGU5NmI0NDc3NGNkYmQyODJjZmE0NTEwZmM5ZjkxMGM3NmY4MzNlNA==--6c4091db0279a8038f650f25e60156921ef0a1d7">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="49027BB0:35CC:2A8E7D10:567F29CA" name="octolytics-dimension-request_id" /><meta content="11814550" name="octolytics-actor-id" /><meta content="edwardvmills" name="octolytics-actor-login" /><meta content="9ef0a9064e375315220363e69084da76587ffa181246d018796dd49c1297b4e9" name="octolytics-actor-hash" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />
<meta content="Rails, view, blob#show" data-pjax-transient="true" name="analytics-event" />


  <meta class="js-ga-set" name="dimension1" content="Logged In">



        <meta name="hostname" content="github.com">
    <meta name="user-login" content="edwardvmills">

        <meta name="expected-hostname" content="github.com">

      <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

    <meta content="7fa31791ad641ee90fdb1ffb53868c02252552f8" name="form-nonce" />

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-16bf5399d85a6f926eb6af8f983ed5cf907e97b4da4a650dc11920d425826218.css" integrity="sha256-Fr9Tmdhab5Jutq+PmD7Vz5B+l7TaSmUNwRkg1CWCYhg=" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github2-451ab63ad67fa9af580e5d9a3b2b7de911ce2e4b2437638f26fe8cb3879e67d8.css" integrity="sha256-RRq2OtZ/qa9YDl2aOyt96RHOLkskN2OPJv6Ms4eeZ9g=" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="be269b1951a3572820c1f935e13a2f75">

      
  <meta name="description" content="NURBSlib_EVM - My python scripts for FreeCAD">
  <meta name="go-import" content="github.com/edwardvmills/NURBSlib_EVM git https://github.com/edwardvmills/NURBSlib_EVM.git">

  <meta content="11814550" name="octolytics-dimension-user_id" /><meta content="edwardvmills" name="octolytics-dimension-user_login" /><meta content="35138129" name="octolytics-dimension-repository_id" /><meta content="edwardvmills/NURBSlib_EVM" name="octolytics-dimension-repository_nwo" /><meta content="false" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="35138129" name="octolytics-dimension-repository_network_root_id" /><meta content="edwardvmills/NURBSlib_EVM" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/edwardvmills/NURBSlib_EVM/commits/master.atom?token=ALRGltYNEnDXYx4peQDmlw_AxXigQ20oks60jFxKwA%3D%3D" rel="alternate" title="Recent Commits to NURBSlib_EVM:master" type="application/atom+xml">

  </head>


  <body class="logged_in   env-production linux vis-private page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>

    
    
    



      <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github "></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/edwardvmills/NURBSlib_EVM/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/edwardvmills/NURBSlib_EVM/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <label class="js-chromeless-input-container form-control">
    <div class="scope-badge">This repository</div>
    <input type="text"
      class="js-site-search-focus js-site-search-field is-clearable chromeless-input"
      data-hotkey="s"
      name="q"
      placeholder="Search"
      aria-label="Search this repository"
      data-global-scope-placeholder="Search GitHub"
      data-repo-scope-placeholder="Search"
      tabindex="1"
      autocapitalize="off">
  </label>
</form>
      </div>

      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item">
          <a href="/pulls" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
            Pull requests
</a>        </li>
        <li class="header-nav-item">
          <a href="/issues" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
            Issues
</a>        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com/" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item">
      <span class="js-socket-channel js-updatable-content"
        data-channel="notification-changed:edwardvmills"
        data-url="/notifications/header">
      <a href="/notifications" aria-label="You have no unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:read" data-hotkey="g n">
          <span class="mail-status all-read"></span>
          <span class="octicon octicon-bell "></span>
</a>  </span>

  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link tooltipped tooltipped-s js-menu-target" href="/new"
       aria-label="Create new…"
       data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus left"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>


  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="edwardvmills/NURBSlib_EVM">This repository</span>
  </div>
    <a class="dropdown-item" href="/edwardvmills/NURBSlib_EVM/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>
    <a class="dropdown-item" href="/edwardvmills/NURBSlib_EVM/settings/collaboration" data-ga-click="Header, create new collaborator">
      New collaborator
    </a>

      </ul>
    </div>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name tooltipped tooltipped-sw js-menu-target" href="/edwardvmills"
       aria-label="View profile and more"
       data-ga-click="Header, show menu, icon:avatar">
      <img alt="@edwardvmills" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/11814550?v=3&amp;s=40" width="20" />
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <div class="dropdown-menu  dropdown-menu-sw">
        <div class=" dropdown-header header-nav-current-user css-truncate">
            Signed in as <strong class="css-truncate-target">edwardvmills</strong>

        </div>


        <div class="dropdown-divider"></div>

          <a class="dropdown-item" href="/edwardvmills" data-ga-click="Header, go to profile, text:your profile">
            Your profile
          </a>
        <a class="dropdown-item" href="/stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a>
        <a class="dropdown-item" href="/explore" data-ga-click="Header, go to explore, text:explore">
          Explore
        </a>
          <a class="dropdown-item" href="/integrations" data-ga-click="Header, go to integrations, text:integrations">
            Integrations
          </a>
        <a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a>

          <div class="dropdown-divider"></div>

          <a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
            Settings
          </a>

          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/logout" class="logout-form" data-form-nonce="7fa31791ad641ee90fdb1ffb53868c02252552f8" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="0yVA8a5IuS6gL5D9gLYtK8aCnrXxp5/KhzcuvemKgSEBH6QK3Hg/Rp7XGkV8+LXsAuXtUp+4ioSz7iMV3tRLOQ==" /></div>
            <button class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
              Sign out
            </button>
</form>
      </div>
    </div>
  </li>
</ul>


    
  </div>
</div>

      

      


    <div id="start-of-content" class="accessibility-aid"></div>

      <div id="js-flash-container">
</div>


    <div role="main" class="main-content">
        <div itemscope itemtype="http://schema.org/WebPage">
    <div id="js-repo-pjax-container" class="context-loader-container js-repo-nav-next" data-pjax-container>
      
<div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
  <div class="container repohead-details-container">

    

<ul class="pagehead-actions">

  <li>
        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-form-nonce="7fa31791ad641ee90fdb1ffb53868c02252552f8" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="N6S1YLkyTqDTHXyfdlxl4bpRPuMsqJ1LhOgChD8+jPl3pqsKl/aL2pUldIVyHQEmrhVqDHLZnJE/XvqfqS8ykg==" /></div>      <input id="repository_id" name="repository_id" type="hidden" value="35138129" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/edwardvmills/NURBSlib_EVM/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
              <span class="octicon octicon-eye "></span>
              Unwatch
            </span>
          </a>
          <a class="social-count js-social-count" href="/edwardvmills/NURBSlib_EVM/watchers">
            1
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span aria-label="Close" class="octicon octicon-x js-menu-close" role="button"></span>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <div class="select-menu-item-text">
                    <input id="do_included" name="do" type="radio" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <span class="octicon octicon-eye"></span>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                  <div class="select-menu-item-text">
                    <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <span class="octicon octicon-eye"></span>
                      Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <div class="select-menu-item-text">
                    <input id="do_ignore" name="do" type="radio" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <span class="octicon octicon-mute"></span>
                      Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/edwardvmills/NURBSlib_EVM/unstar" class="js-toggler-form starred js-unstar-button" data-form-nonce="7fa31791ad641ee90fdb1ffb53868c02252552f8" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="fo9NfHZ4PLWyOeaDrFpl8IcNv7YAr3clhvKR6QT7fbP2ZUmfKhmfoQB39NOWb4OGgvTWxIKSvrOoTg8W3AXrpg==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar edwardvmills/NURBSlib_EVM"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <span class="octicon octicon-star "></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/edwardvmills/NURBSlib_EVM/stargazers">
          0
        </a>
</form>
    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/edwardvmills/NURBSlib_EVM/star" class="js-toggler-form unstarred js-star-button" data-form-nonce="7fa31791ad641ee90fdb1ffb53868c02252552f8" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="HUTHJrocy4tgovtukZpehhKlhTP4jGk8JHkkoH7TaxCfVYKDeIzdBLC14PdRbZ1+iZRSuYlh2MIg72sEtmJYng==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star edwardvmills/NURBSlib_EVM"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <span class="octicon octicon-star "></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/edwardvmills/NURBSlib_EVM/stargazers">
          0
        </a>
</form>  </div>

  </li>

  <li>
          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/edwardvmills/NURBSlib_EVM/fork" class="btn-with-count" data-form-nonce="7fa31791ad641ee90fdb1ffb53868c02252552f8" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Cb7TgLjN1QYwxDVGN9SZfJvo8MkqO3paaYAVKsSg2Qc3D4iOXQFK2CdXsevry0aMTJOYUzmVUNNQRODa6ULfFQ==" /></div>
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of edwardvmills/NURBSlib_EVM to your account"
                aria-label="Fork your own copy of edwardvmills/NURBSlib_EVM to your account">
              <span class="octicon octicon-repo-forked "></span>
              Fork
            </button>
</form>
    <a href="/edwardvmills/NURBSlib_EVM/network" class="social-count">
      0
    </a>
  </li>
</ul>

    <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title private ">
  <span class="octicon octicon-lock "></span>
  <span class="author"><a href="/edwardvmills" class="url fn" itemprop="url" rel="author"><span itemprop="title">edwardvmills</span></a></span><!--
--><span class="path-divider">/</span><!--
--><strong><a href="/edwardvmills/NURBSlib_EVM" data-pjax="#js-repo-pjax-container">NURBSlib_EVM</a></strong>
    <span class="repo-private-label">private</span>

  <span class="page-context-loader">
    <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
  </span>

</h1>

  </div>
  <div class="container">
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <a href="/edwardvmills/NURBSlib_EVM" aria-label="Code" aria-selected="true" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /edwardvmills/NURBSlib_EVM">
    <span class="octicon octicon-code "></span>
    Code
</a>
    <a href="/edwardvmills/NURBSlib_EVM/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /edwardvmills/NURBSlib_EVM/issues">
      <span class="octicon octicon-issue-opened "></span>
      Issues
      <span class="counter">0</span>
</a>
  <a href="/edwardvmills/NURBSlib_EVM/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /edwardvmills/NURBSlib_EVM/pulls">
    <span class="octicon octicon-git-pull-request "></span>
    Pull requests
    <span class="counter">0</span>
</a>
    <a href="/edwardvmills/NURBSlib_EVM/wiki" class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /edwardvmills/NURBSlib_EVM/wiki">
      <span class="octicon octicon-book "></span>
      Wiki
</a>
  <a href="/edwardvmills/NURBSlib_EVM/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /edwardvmills/NURBSlib_EVM/pulse">
    <span class="octicon octicon-pulse "></span>
    Pulse
</a>
  <a href="/edwardvmills/NURBSlib_EVM/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /edwardvmills/NURBSlib_EVM/graphs">
    <span class="octicon octicon-graph "></span>
    Graphs
</a>
    <a href="/edwardvmills/NURBSlib_EVM/settings" class="js-selected-navigation-item reponav-item" data-selected-links="repo_settings repo_branch_settings hooks /edwardvmills/NURBSlib_EVM/settings">
      <span class="octicon octicon-gear "></span>
      Settings
</a>
</nav>

  </div>
</div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    

<a href="/edwardvmills/NURBSlib_EVM/blob/8ddcf98cf817398cbd146935719414f68ad71775/README.md" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:e660b7aba58facfce3d868383fc22253 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <button class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    title="master"
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span aria-label="Close" class="octicon octicon-x js-menu-close" role="button"></span>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Find or create a branch…" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/edwardvmills/NURBSlib_EVM/blob/gh-pages/README.md"
               data-name="gh-pages"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="gh-pages">
                gh-pages
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/edwardvmills/NURBSlib_EVM/blob/master/README.md"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
        </div>

          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/edwardvmills/NURBSlib_EVM/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" data-form-nonce="7fa31791ad641ee90fdb1ffb53868c02252552f8" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="oppdo7DUWIKWftMe+L+z30p2SD0C/gFHrb0N/yEFHMIZqxE7ZCGuGNUAToncE3IHsB9qSAHWHUzrO4AaWBXL7w==" /></div>
            <span class="octicon octicon-git-branch select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <span class="select-menu-item-heading">Create branch: <span class="js-new-item-name"></span></span>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master">
            <input type="hidden" name="path" id="path" value="README.md">
</form>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/edwardvmills/NURBSlib_EVM/find/master"
          class="js-show-file-finder btn btn-sm"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/edwardvmills/NURBSlib_EVM" class="" data-branch="master" data-pjax="true" itemscope="url"><span itemprop="title">NURBSlib_EVM</span></a></span></span><span class="separator">/</span><strong class="final-path">README.md</strong>
  </div>
</div>


  <div class="commit-tease">
      <span class="right">
        <a class="commit-tease-sha" href="/edwardvmills/NURBSlib_EVM/commit/41af9e761e81b0dcbf7eec1cc6fae2c26d5e3e3d" data-pjax>
          41af9e7
        </a>
        <time datetime="2015-12-25T23:13:27Z" is="relative-time">Dec 25, 2015</time>
      </span>
      <div>
        <img alt="@edwardvmills" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/11814550?v=3&amp;s=40" width="20" />
        <a href="/edwardvmills" class="user-mention" rel="author">edwardvmills</a>
          <a href="/edwardvmills/NURBSlib_EVM/commit/41af9e761e81b0dcbf7eec1cc6fae2c26d5e3e3d" class="message" data-pjax="true" title="Update README.md">Update README.md</a>
      </div>

    <div class="commit-tease-contributors">
      <a class="muted-link contributors-toggle" href="#blob_contributors_box" rel="facebox">
        <strong>1</strong>
         contributor
      </a>
      
    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@edwardvmills" height="24" src="https://avatars3.githubusercontent.com/u/11814550?v=3&amp;s=48" width="24" />
            <a href="/edwardvmills">edwardvmills</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="btn-group">
      <a href="/edwardvmills/NURBSlib_EVM/raw/master/README.md" class="btn btn-sm " id="raw-url">Raw</a>
        <a href="/edwardvmills/NURBSlib_EVM/blame/master/README.md" class="btn btn-sm js-update-url-with-hash">Blame</a>
      <a href="/edwardvmills/NURBSlib_EVM/commits/master/README.md" class="btn btn-sm " rel="nofollow">History</a>
    </div>


        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/edwardvmills/NURBSlib_EVM/edit/master/README.md" class="inline-form js-update-url-with-hash" data-form-nonce="7fa31791ad641ee90fdb1ffb53868c02252552f8" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="wTZAinjGtyx94a//IF9gFboIYs7aaWBjG3R9sGgnixeP9H70mhrYXKK9wBGPq1k8i59//k/aEMhhe/0Q6qt2Rw==" /></div>
          <button class="octicon-btn tooltipped tooltipped-nw" type="submit"
            aria-label="Edit this file" data-hotkey="e" data-disable-with>
            <span class="octicon octicon-pencil "></span>
          </button>
</form>        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/edwardvmills/NURBSlib_EVM/delete/master/README.md" class="inline-form" data-form-nonce="7fa31791ad641ee90fdb1ffb53868c02252552f8" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="vka9DJ8LDmXpcRhzAujN0Fu6Oz4I50AR8HYSCMroO+5nHHyQUdIKy7MXdEf9UH3VgWKgw3UTms9io8OKL0d0nw==" /></div>
          <button class="octicon-btn octicon-btn-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Delete this file" data-disable-with>
            <span class="octicon octicon-trashcan "></span>
          </button>
</form>  </div>

  <div class="file-info">
      61 lines (41 sloc)
      <span class="file-info-divider"></span>
    6.15 KB
  </div>
</div>

  
  <div id="readme" class="blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="mainContentOfPage"><h2><a id="user-content-nurbslib_evm" class="anchor" href="#nurbslib_evm" aria-hidden="true"><span class="octicon octicon-link"></span></a>NURBSlib_EVM</h2>

<p>My python scripts for creating surfaces in <a href="http://freecadweb.org/">FreeCAD</a>.   </p>

<p>At this time, none of the entities created by these scripts are parametric. This is the rough workflow prototyping phase. If/when the surface creation methods reach my minimum goals, i intend to make them parametric.</p>

<p>The ultimate goal is to implement a set of tools that require <em>very few points and tangents/normals</em> to generate NURBS surfaces of high continuity. I have some ideas as to what constitutes an efficient and intuitive input/interface structure. This is very personal, and cannot address all individual preferences. </p>

<p>Ideally, the user interaction with the points/normals would be analogous to manipulating a coarse mesh, like subdivision surfaces. The main difference with subdivision surfaces being that with full NURBS, we can have perfect conics, no intrinsic continuity limits, and the 'handles' <i>stay on the surface itself</i>. So when we dimension/constrain the handles, we are dimensioning the surface itself.</p>

<p>What this means in practice is that eventually the user will not need to know <em>anything</em> about control points, knot vectors, or weights. At this stage however, a minimum understanding of control points is still necessary to use the tools.</p>

<p><strong>These are not the 'classic' surfacing tools like sweep, loft, blend, trim, etc</strong>, although there are many parallels.<br>
FreeCAD already has some of these tools in the Part module and i believe the PartDesign module is slated to get improved versions soon. OpenCascade itself already has all of these functions built in, but i am not a programmer, so i cannot use OpenCascade directly. </p>

<p>All scripts in this repository are offered under the terms of the <a href="http://www.gnu.org/licenses/gpl-3.0.en.html">GPLv3</a><br>
All models in this repository are offered under the terms of <a href="http://creativecommons.org/licenses/by/2.0/">CC-BY</a></p>

<h3><a id="user-content-in-this-repo" class="anchor" href="#in-this-repo" aria-hidden="true"><span class="octicon octicon-link"></span></a>In this repo:</h3>

<p>-a single .py with all the 'geometry' functions, where i try to use the most basic inputs.<br>
-individual .fcmacro files that tie the current GUI and selection behavior of FreeCAD to single modeling operations.<br>
-various utility .fcmacro functions to assist in creating sketches ('handles') to pass to the NURBS tools.<br>
-test FreeCAD model files. These model files are irrelevant to the scripts, i keep them in the repo for my ease of access. </p>

<hr>

<h3><a id="user-content-setup" class="anchor" href="#setup" aria-hidden="true"><span class="octicon octicon-link"></span></a>Setup</h3>

<p>-from the top level of the repository, take NURBSlib_EVM.py, all  *.fcmacro files, and the icons folder
-put them somewhere FreeCAD can find them<br>
-link the fcmacro scripts to icons, descriptions, tooltips, etc. 
-put all those GUI macros in toolbars.<br>
-add that toolbar to the PartDesign workbench. The raw material will be PartDesign sketches, so this is a good place to put the toolbars for the time being.   </p>

<p><a href="http://freecadweb.org/wiki/index.php?title=Macros">instructions for toolbars/macros in FreeCAD</a> </p>

<h3><a id="user-content-usage-basic-knowledge-of-the-freecad-partdesign-sketcher-is-required" class="anchor" href="#usage-basic-knowledge-of-the-freecad-partdesign-sketcher-is-required" aria-hidden="true"><span class="octicon octicon-link"></span></a>Usage (basic knowledge of the FreeCAD PartDesign Sketcher is required)</h3>

<p>More details on usage will be made available <a href="http://edwardvmills.github.io/NURBSlib_EVM/">here</a> as time permits.</p>

<p>-draw sketches of lines/circles (read the curve macros to see what inputs they want)<br>
-select those lines/circles in the order specified by the macro, then hit the macro button &gt; curve is created.<br>
-select 3/4 curves in a loop counterclockwise (surface normal will then point towards you), hit the surface macro button &gt; surface is created.</p>

<p>The surfaces are 100% controlled by the curves, which are 100% controlled by the sketches. This can be very powerful, but requires following strict rules for the sketches to obtain good results. Utilities to control the sketches and continuity are in various stages of planning/prototyping. I suspect much could already be done by using spreadsheets and expressions.</p>

<hr>

<h3><a id="user-content-nurbs-in-general-and-what-these-scripts-are-trying-to-do" class="anchor" href="#nurbs-in-general-and-what-these-scripts-are-trying-to-do" aria-hidden="true"><span class="octicon octicon-link"></span></a>NURBS in general, and what these scripts are trying to do</h3>

<p>For now, my focus is on skinning sets of 3 or 4 curves in a loop. </p>

<p>The skinning routines should be 
-<em>repeatable</em>: produce the same result for the same inputs
-<em>consistent</em>: produce a scaled result for a scaled input. </p>

<p>The seams joining adjacent surfaces should always have the same level of continuity as the adjacent curves at the surface corners.</p>

<p>I am learning as i go, so i am trying to 'juice' the most out of the basic NURBS formulations before moving on to more complex forms. High degrees and complex knot vectors give great smoothness, but few of the control points correspond to actual surface points, so they are challenging to fit among other engineering forms and constrain correctly.</p>

<p>The cubic bezier form is the simplest form that can connect two points with specified tangents (G1), and i am exploring its limits. The weight control interface is incomplete, but curve weights are incorporated into the surfaces in a crude way. Arcs can be converted to rational Bezier and used in surfaces. I have a basic quadrilateral surface patch, and a rudimentary triangular suface patch (one collapsed edge/corner). It is theoretically possible to modify the inner control points and weights of a bezier to control the curvature (G2) across the seams in some cases, but this requires manipulating several control points at once, and maintaining tangent continuity is hard to begin with.</p>

<p>For now, the Bezier curves and surfaces are considered to be 'rough drafts' of the final surfaces. Easy to specify, cheap to tesselate. Sometimes they may even be adequate to patch a hole in a shell, if the surrounding surfaces are simple.</p>

<p>In order to have isolated curvature at each curve endpoint, i made a 6 control point cubic curve and associated 6X6 surface. This surface type does not have a triangle version yet. Included are utilites to convert cubic Bezier and arcs to this curve type.   </p>

<p>This will open up the possibility of using the 3rd and 4th points to control start and end curvature respectively. This can be done without interfering with the use of the 2nd and 5th control points to set tangents. Right now the curvature matching must be done by hand, but for any particular value of curvature desired at a curve connection, there are many possible control points positions. These additional degrees of freedom will (i hope) allow the possibility of controlling the derivative of curvature (highlight flow).</p>
</article>
  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

  </div>
  <div class="modal-backdrop"></div>
</div>

    </div>
  </div>

    </div>

        <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>
        <li><a href="https://github.com/pricing" data-ga-click="Footer, go to pricing, text:pricing">Pricing</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github " title="GitHub "></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.06250s from github-fe134-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



    
    
    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
        <span class="octicon octicon-x"></span>
      </button>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" integrity="sha256-7460qJ7p88i3YTMH/liaj1cFgX987ie+xRzl6WMjSr8=" src="https://assets-cdn.github.com/assets/frameworks-ef8eb4a89ee9f3c8b7613307fe589a8f5705817f7cee27bec51ce5e963234abf.js"></script>
      <script async="async" crossorigin="anonymous" integrity="sha256-S2uOfRHrt7zoUSbTtBMMgAQfKubV1u+JAajAw/fLgNI=" src="https://assets-cdn.github.com/assets/github-4b6b8e7d11ebb7bce85126d3b4130c80041f2ae6d5d6ef8901a8c0c3f7cb80d2.js"></script>
      
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner hidden">
      <span class="octicon octicon-alert"></span>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
  </body>
</html>

