# MP-Nextion
Communicat easy with Nextion-Display in MicroPython

Just [Read the docs](https://github.com/Dennis-89/MP-Nextion/blob/main/docs/build/html/index.html) and have fun!



<!DOCTYPE html>
<html class="writer-html5" lang="en" data-content_root="./">
<head>
  <meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1" />

  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MP-Nextion documentation &mdash; MP-Nextion  documentation</title>
      <link rel="stylesheet" type="text/css" href="_static/pygments.css?v=b86133f3" />
      <link rel="stylesheet" type="text/css" href="_static/css/theme.css?v=9edc463e" />

  
      <script src="_static/jquery.js?v=5d32c60e"></script>
      <script src="_static/_sphinx_javascript_frameworks_compat.js?v=2cd50e6c"></script>
      <script src="_static/documentation_options.js?v=5929fcd5"></script>
      <script src="_static/doctools.js?v=fd6eb6e6"></script>
      <script src="_static/sphinx_highlight.js?v=6ffebe34"></script>
    <script src="_static/js/theme.js"></script>
    <link rel="index" title="Index" href="genindex.html" />
    <link rel="search" title="Search" href="search.html" /> 
</head>

<body class="wy-body-for-nav"> 
  <div class="wy-grid-for-nav">
    <nav data-toggle="wy-nav-shift" class="wy-nav-side">
      <div class="wy-side-scroll">
        <div class="wy-side-nav-search" >

          
          
          <a href="#" class="icon icon-home">
            MP-Nextion
          </a>
<div role="search">
  <form id="rtd-search-form" class="wy-form" action="search.html" method="get">
    <input type="text" name="q" placeholder="Search docs" aria-label="Search docs" />
    <input type="hidden" name="check_keywords" value="yes" />
    <input type="hidden" name="area" value="default" />
  </form>
</div>
        </div><div class="wy-menu wy-menu-vertical" data-spy="affix" role="navigation" aria-label="Navigation menu">
              <!-- Local TOC -->
              <div class="local-toc"><ul>
<li><a class="reference internal" href="#">MP-Nextion documentation</a><ul>
<li><a class="reference internal" href="#Nextion.Nextion"><code class="docutils literal notranslate"><span class="pre">Nextion</span></code></a><ul>
<li><a class="reference internal" href="#Nextion.Nextion.__init__"><code class="docutils literal notranslate"><span class="pre">Nextion.__init__()</span></code></a></li>
<li><a class="reference internal" href="#Nextion.Nextion.brightness"><code class="docutils literal notranslate"><span class="pre">Nextion.brightness()</span></code></a></li>
<li><a class="reference internal" href="#Nextion.Nextion.change_page"><code class="docutils literal notranslate"><span class="pre">Nextion.change_page()</span></code></a></li>
<li><a class="reference internal" href="#Nextion.Nextion.cmd"><code class="docutils literal notranslate"><span class="pre">Nextion.cmd()</span></code></a></li>
<li><a class="reference internal" href="#Nextion.Nextion.read"><code class="docutils literal notranslate"><span class="pre">Nextion.read()</span></code></a></li>
<li><a class="reference internal" href="#Nextion.Nextion.reset"><code class="docutils literal notranslate"><span class="pre">Nextion.reset()</span></code></a></li>
<li><a class="reference internal" href="#Nextion.Nextion.sleep"><code class="docutils literal notranslate"><span class="pre">Nextion.sleep()</span></code></a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
        </div>
      </div>
    </nav>

    <section data-toggle="wy-nav-shift" class="wy-nav-content-wrap"><nav class="wy-nav-top" aria-label="Mobile navigation menu" >
          <i data-toggle="wy-nav-top" class="fa fa-bars"></i>
          <a href="#">MP-Nextion</a>
      </nav>

      <div class="wy-nav-content">
        <div class="rst-content">
          <div role="navigation" aria-label="Page navigation">
  <ul class="wy-breadcrumbs">
      <li><a href="#" class="icon icon-home" aria-label="Home"></a></li>
      <li class="breadcrumb-item active">MP-Nextion documentation</li>
      <li class="wy-breadcrumbs-aside">
            <a href="_sources/index.rst.txt" rel="nofollow"> View page source</a>
      </li>
  </ul>
  <hr/>
</div>
          <div role="main" class="document" itemscope="itemscope" itemtype="http://schema.org/Article">
           <div itemprop="articleBody">
             
  <section id="mp-nextion-documentation">
<h1>MP-Nextion documentation<a class="headerlink" href="#mp-nextion-documentation" title="Link to this heading"></a></h1>
<p>To communicate easy with the Nextion-Display in MicroPython.</p>
<dl class="py class">
<dt class="sig sig-object py" id="Nextion.Nextion">
<span class="property"><span class="k"><span class="pre">class</span></span><span class="w"> </span></span><span class="sig-prename descclassname"><span class="pre">Nextion.</span></span><span class="sig-name descname"><span class="pre">Nextion</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">baudrate</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">tx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">10</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">rx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">9</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">get_page_event</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">start_page</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#Nextion.Nextion" title="Link to this definition"></a></dt>
<dd><dl class="py method">
<dt class="sig sig-object py" id="Nextion.Nextion.__init__">
<span class="sig-name descname"><span class="pre">__init__</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">baudrate</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">tx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">10</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">rx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">9</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">get_page_event</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">start_page</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#Nextion.Nextion.__init__" title="Link to this definition"></a></dt>
<dd><p>UART channel is 1.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>baudrate</strong> – Check out the display’s instructions. E.g. 9600</p></li>
<li><p><strong>tx</strong> – The tx-Pin you want to use.</p></li>
<li><p><strong>rx</strong> – The rx-Pin you want to use.</p></li>
<li><p><strong>get_page_event</strong> – If True, it detects page switching.To do this,
you have to write the preinitialize event for each page:
<cite>printh 23 02 50 xx</cite>. <cite>xx</cite> is the page number in hex.
For page 0: <cite>printh 23 02 50 00</cite>. For page 10: <cite>printh 23 02 50 0A</cite>.
Now you can get the current page with <cite>Nextion.current_page</cite>.
You can also set locked page with <cite>Nextion.lock_pages.add(&lt;page number&gt;)</cite></p></li>
<li><p><strong>start_page</strong> – If the first displayed page isn’t page-id 0, set them here.
This is needed for <cite>get_page_event</cite></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="Nextion.Nextion.brightness">
<span class="sig-name descname"><span class="pre">brightness</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">brightness</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#Nextion.Nextion.brightness" title="Link to this definition"></a></dt>
<dd><p>Dim the display</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>brightness</strong> – Values from 0…100</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>None</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="Nextion.Nextion.change_page">
<span class="sig-name descname"><span class="pre">change_page</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">page</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#Nextion.Nextion.change_page" title="Link to this definition"></a></dt>
<dd><p>Change the page of the display.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>page</strong> – The name or the id of the page
you want to go to.</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>None</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="Nextion.Nextion.cmd">
<span class="sig-name descname"><span class="pre">cmd</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">command</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">write_and_read</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#Nextion.Nextion.cmd" title="Link to this definition"></a></dt>
<dd><p>Send one of the Nextion-specific commands to the display.
See: <a class="reference external" href="https://nextion.tech/instruction-set/">https://nextion.tech/instruction-set/</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>command</strong> – The command you want to send</p></li>
<li><p><strong>write_and_read</strong> – If True(default), return a <cite>UART.read()</cite> object
else return None</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>UART.read() or None</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="Nextion.Nextion.read">
<span class="sig-name descname"><span class="pre">read</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">raw</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#Nextion.Nextion.read" title="Link to this definition"></a></dt>
<dd><p>Read the rx-line.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>raw</strong> – If True, the raw values are returned without decoding.
If False (default), the values are decoded to <cite>ascii</cite></p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>UART.read() decoded or not. None if there aren’t values
of if there is an error while decoding.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="Nextion.Nextion.reset">
<span class="sig-name descname"><span class="pre">reset</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#Nextion.Nextion.reset" title="Link to this definition"></a></dt>
<dd><p>Resets the Display</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="Nextion.Nextion.sleep">
<span class="sig-name descname"><span class="pre">sleep</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">state</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#Nextion.Nextion.sleep" title="Link to this definition"></a></dt>
<dd><p>Sets display in sleep or awake mode</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – If True, sleep-mode is on, else sleep-mode is off</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>None</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

</section>


           </div>
          </div>
          <footer>

  <hr/>

  <div role="contentinfo">
    <p>&#169; Copyright 2026, D.Straub.</p>
  </div>

  Built with <a href="https://www.sphinx-doc.org/">Sphinx</a> using a
    <a href="https://github.com/readthedocs/sphinx_rtd_theme">theme</a>
    provided by <a href="https://readthedocs.org">Read the Docs</a>.
   

</footer>
        </div>
      </div>
    </section>
  </div>
  <script>
      jQuery(function () {
          SphinxRtdTheme.Navigation.enable(true);
      });
  </script> 

</body>
</html>
