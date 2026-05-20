(function () {
  let projects = Array.isArray(window.PROJECTS) ? window.PROJECTS : [];
  const lang = document.documentElement.lang.toLowerCase().startsWith("en") ? "en" : "zh";
  const assetBase = new URL(".", document.currentScript.src);
  const assetPath = (path) => new URL(path, assetBase).toString();

  const copy = {
    zh: {
      countAll: "个项目",
      countCategory: (label) => `个${label}项目`,
      itemCount: "个项目",
      empty: "没有匹配的项目，换一个关键词试试。",
      details: "查看详情",
      categoryAlt: (label) => `${label}分类图`,
      projectAlt: (name) => `${name}项目分类图`,
      dialogImageAlt: (name) => `${name}项目图`,
      functionTitle: "实现功能",
      techTitle: "核心器件 / 技术",
      materialsTitle: "可确认物料",
      resourceTitle: "项目资源",
      accessTitle: "获取说明",
      sourceUrl: "源码链接",
      demoVideoUrl: "演示视频",
      configDocUrl: "配置文档",
      accessText: (subject) =>
        `公开页面不展示源码仓库地址。咨询时可发送“${subject}”，确认后按项目交付资料包或私有仓库访问方式。`,
      deliverables: {
        source: "源码工程",
        docs: "设计文档",
        hardware: "硬件资料",
        report: "报告参考",
        software: "软件端资料",
        cloud: "联网配置",
      },
      levels: {
        beginner: "入门型",
        intermediate: "进阶型",
        comprehensive: "综合型",
      },
    },
    en: {
      countAll: "projects",
      countCategory: (label) => `${label.toLowerCase()} projects`,
      itemCount: "projects",
      empty: "No matching projects. Try another keyword.",
      details: "Details",
      categoryAlt: (label) => `${label} category image`,
      projectAlt: (name) => `${name} category image`,
      dialogImageAlt: (name) => `${name} image`,
      functionTitle: "Implemented Functions",
      techTitle: "Key Materials / Technologies",
      materialsTitle: "Confirmable Deliverables",
      resourceTitle: "Project Resources",
      accessTitle: "Access Note",
      sourceUrl: "Source Link",
      demoVideoUrl: "Demo Video",
      configDocUrl: "Config Document",
      accessText: (subject) =>
        `The public page does not expose source repository URLs. You can send "${subject}" when requesting materials; delivery is confirmed separately through a project package or private repository access.`,
      deliverables: {
        source: "Source Code",
        docs: "Design Documents",
        hardware: "Hardware Materials",
        report: "Report References",
        software: "Software-side Materials",
        cloud: "Cloud / Network Config",
      },
      levels: {
        beginner: "Beginner",
        intermediate: "Intermediate",
        comprehensive: "Comprehensive",
      },
    },
  };

  const categories = [
    {
      id: "all",
      label: { zh: "全部项目", en: "All Projects" },
      caption: { zh: "完整索引", en: "Full catalog" },
      image: assetPath("images/hero/hero-board.png"),
      keywords: [],
    },
    {
      id: "environment",
      label: { zh: "环境监测", en: "Environment Monitoring" },
      caption: { zh: "传感器 / 报警 / 显示", en: "Sensors / alarms / display" },
      image: assetPath("images/categories/category-environment.png"),
      keywords: [
        "环境",
        "温湿度",
        "空气",
        "水质",
        "粉尘",
        "PH",
        "pH",
        "CO2",
        "甲醛",
        "烟雾",
        "水位",
        "液位",
        "气体",
        "酒精",
        "浊度",
        "TDS",
        "紫外线",
        "光照",
        "厂房",
        "压力",
        "压强",
        "environment",
        "temperature",
        "humidity",
        "air",
        "water quality",
        "dust",
        "formaldehyde",
        "smoke",
        "liquid level",
        "gas",
        "alcohol",
        "turbidity",
        "ultraviolet",
        "light",
        "pressure",
        "factory",
      ],
    },
    {
      id: "iot",
      label: { zh: "农业 / 物联网", en: "Agriculture / IoT" },
      caption: { zh: "云平台 / APP / 远程", en: "Cloud / APP / remote" },
      image: assetPath("images/categories/category-iot.png"),
      keywords: [
        "农业",
        "大棚",
        "温室",
        "灌溉",
        "养殖",
        "云平台",
        "OneNET",
        "ONENET",
        "阿里云",
        "IoT",
        "ESP",
        "WiFi",
        "4G",
        "远程",
        "APP",
        "App",
        "小程序",
        "Uniapp",
        "UNIAPP",
        "蓝牙",
        "agriculture",
        "greenhouse",
        "irrigation",
        "aquaculture",
        "cloud",
        "Aliyun",
        "Bluetooth",
        "remote",
        "mini-program",
        "mobile",
      ],
    },
    {
      id: "home",
      label: { zh: "智能家居", en: "Smart Home" },
      caption: { zh: "生活场景 / 设备联动", en: "Daily scenarios / linked devices" },
      image: assetPath("images/categories/category-home.png"),
      keywords: [
        "家居",
        "窗帘",
        "台灯",
        "热水器",
        "闹钟",
        "时钟",
        "宿舍",
        "寝室",
        "宠物",
        "鱼缸",
        "垃圾桶",
        "空气净化器",
        "电梯",
        "home",
        "curtain",
        "lamp",
        "water heater",
        "clock",
        "alarm clock",
        "dormitory",
        "pet",
        "fish tank",
        "bin",
        "garbage",
        "air purifier",
        "elevator",
      ],
    },
    {
      id: "security",
      label: { zh: "安防门禁", en: "Security Access" },
      caption: { zh: "识别 / 报警 / 消防", en: "Recognition / alarm / fire safety" },
      image: assetPath("images/categories/category-security.png"),
      keywords: [
        "安防",
        "门禁",
        "密码锁",
        "指纹",
        "人脸",
        "报警",
        "消防",
        "火焰",
        "防盗",
        "加油站",
        "安全",
        "红外",
        "人体",
        "security",
        "access control",
        "password",
        "fingerprint",
        "face recognition",
        "alarm",
        "fire",
        "flame",
        "anti-theft",
        "gas station",
        "safety",
        "infrared",
        "PIR",
      ],
    },
    {
      id: "health",
      label: { zh: "健康医疗", en: "Health Monitoring" },
      caption: { zh: "体征 / 可穿戴 / 监护", en: "Vital signs / wearable / care" },
      image: assetPath("images/categories/category-health.png"),
      keywords: [
        "心率",
        "血氧",
        "体温",
        "血压",
        "健康",
        "可穿戴",
        "手环",
        "姿态",
        "计步",
        "婴儿",
        "医疗",
        "称重",
        "heart rate",
        "SpO2",
        "blood oxygen",
        "body temperature",
        "blood pressure",
        "health",
        "wearable",
        "wristband",
        "posture",
        "pedometer",
        "infant",
        "medical",
        "weighing",
      ],
    },
    {
      id: "motion",
      label: { zh: "运动控制", en: "Motion Control" },
      caption: { zh: "电机 / 舵机 / PWM", en: "Motor / servo / PWM" },
      image: assetPath("images/categories/category-motion.png"),
      keywords: [
        "电机",
        "舵机",
        "步进",
        "小车",
        "机械臂",
        "机器人",
        "PWM",
        "调速",
        "运动",
        "分拣",
        "颜色识别",
        "motor",
        "servo",
        "stepper",
        "car",
        "robot",
        "robotic arm",
        "speed control",
        "motion",
        "sorting",
        "color recognition",
      ],
    },
    {
      id: "data",
      label: { zh: "数据采集 / 通信", en: "Data / Communication" },
      caption: { zh: "ADC / 串口 / 上位机", en: "ADC / serial / PC software" },
      image: assetPath("images/categories/category-data.png"),
      keywords: [
        "ADC",
        "DAC",
        "串口",
        "上位机",
        "RS485",
        "IIC",
        "SPI",
        "SD卡",
        "Flash",
        "频率",
        "示波器",
        "采集",
        "通信",
        "SIM",
        "数据",
        "测量",
        "serial",
        "PC software",
        "SD card",
        "frequency",
        "oscilloscope",
        "acquisition",
        "communication",
        "measurement",
        "data",
      ],
    },
  ];

  const state = {
    category: "all",
    query: "",
    sort: "id",
    visible: 24,
  };

  const els = {
    categoryGrid: document.querySelector("#categoryGrid"),
    projectGrid: document.querySelector("#projectGrid"),
    search: document.querySelector("#projectSearch"),
    sort: document.querySelector("#sortSelect"),
    resultCount: document.querySelector("#resultCount"),
    resultText: document.querySelector("#resultText"),
    loadMore: document.querySelector("#loadMoreButton"),
    dialog: document.querySelector("#projectDialog"),
    dialogContent: document.querySelector("#dialogContent"),
    statTotal: document.querySelector("[data-stat='total']"),
  };

  function escapeHtml(value) {
    return String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function textOf(project) {
    const materials = Array.isArray(project.materials) ? project.materials.join(" ") : "";
    return `${project.id} ${project.name || ""} ${project.description || ""} ${project.tech || ""} ${materials}`;
  }

  function labelOf(category) {
    return category.label[lang];
  }

  function captionOf(category) {
    return category.caption[lang];
  }

  function scoreCategory(project, category) {
    if (category.id === "all") return 1;
    const text = textOf(project).toLowerCase();
    return category.keywords.reduce((score, keyword) => {
      return text.includes(String(keyword).toLowerCase()) ? score + 1 : score;
    }, 0);
  }

  function matchesCategory(project, categoryId) {
    if (categoryId === "all") return true;
    const category = categories.find((item) => item.id === categoryId);
    return category ? scoreCategory(project, category) > 0 : true;
  }

  function primaryCategory(project) {
    let selected = categories[categories.length - 1];
    let bestScore = 0;
    categories.slice(1).forEach((category) => {
      const score = scoreCategory(project, category);
      if (score > bestScore) {
        bestScore = score;
        selected = category;
      }
    });
    return selected;
  }

  function techItems(project) {
    return String(project.tech || "")
      .split(/[、,+/]/)
      .map((item) => item.trim())
      .filter(Boolean)
      .slice(0, 16);
  }

  function inferDeliverables(project) {
    if (Array.isArray(project.materials) && project.materials.length > 0) {
      return project.materials;
    }

    const text = textOf(project);
    const names = copy[lang].deliverables;
    const deliverables = [names.source, names.docs];

    if (/PCB|schematic|wiring|hardware|sensor|module|circuit|原理图|接线|硬件|传感器|模块|电路/i.test(text)) {
      deliverables.push(names.hardware);
    }
    if (/report|thesis|paper|flowchart|diagram|论文|报告|LW|流程图|系统框图|Visio/i.test(text)) {
      deliverables.push(names.report);
    }
    if (/APP|application|PC|software|Python|mini-program|Android|小程序|上位机|安卓|Uniapp|UNIAPP/i.test(text)) {
      deliverables.push(names.software);
    }
    if (/Aliyun|OneNET|ONENET|cloud|MQTT|WiFi|ESP|4G|阿里云|云平台/i.test(text)) {
      deliverables.push(names.cloud);
    }

    return Array.from(new Set(deliverables));
  }

  function inferLevel(project) {
    const itemCount = techItems(project).length;
    const text = textOf(project);
    const levels = copy[lang].levels;
    if (/FreeRTOS|RTOS|RTThread|PC software|APP|application|mini-program|Aliyun|OneNET|ONENET|cloud|4G|上位机|小程序|阿里云/i.test(text) || itemCount >= 9) {
      return levels.comprehensive;
    }
    if (itemCount <= 4) {
      return levels.beginner;
    }
    return levels.intermediate;
  }

  function projectImage(project, category) {
    return project.imageUrl || project.image || category.image;
  }

  function resourceLinks(project) {
    return [
      ["sourceUrl", copy[lang].sourceUrl],
      ["demoVideoUrl", copy[lang].demoVideoUrl],
      ["configDocUrl", copy[lang].configDocUrl],
    ]
      .map(([key, label]) => ({ label, url: String(project[key] || "").trim() }))
      .filter((item) => item.url);
  }

  function projectMatchesQuery(project) {
    const query = state.query.trim().toLowerCase();
    if (!query) return true;
    return textOf(project).toLowerCase().includes(query);
  }

  function filteredProjects() {
    const list = projects.filter((project) => {
      return matchesCategory(project, state.category) && projectMatchesQuery(project);
    });

    return list.sort((a, b) => {
      const locale = lang === "zh" ? "zh-Hans-CN" : "en";
      if (state.sort === "name") return a.name.localeCompare(b.name, locale);
      if (state.sort === "category") {
        return labelOf(primaryCategory(a)).localeCompare(labelOf(primaryCategory(b)), locale) || a.id - b.id;
      }
      return a.id - b.id;
    });
  }

  function renderCategories() {
    const html = categories
      .map((category) => {
        const count = category.id === "all"
          ? projects.length
          : projects.filter((project) => matchesCategory(project, category.id)).length;
        const active = state.category === category.id ? " is-active" : "";
        const label = labelOf(category);
        return `
          <button class="category-card${active}" type="button" data-category="${escapeHtml(category.id)}">
            <img src="${escapeHtml(category.image)}" alt="${escapeHtml(copy[lang].categoryAlt(label))}" loading="lazy">
            <span>${count} ${escapeHtml(copy[lang].itemCount)}</span>
            <strong>${escapeHtml(label)}</strong>
            <small>${escapeHtml(captionOf(category))}</small>
          </button>
        `;
      })
      .join("");
    els.categoryGrid.innerHTML = html;
  }

  function renderProjects() {
    const list = filteredProjects();
    const visibleList = list.slice(0, state.visible);
    const activeCategory = categories.find((item) => item.id === state.category);
    els.resultCount.textContent = list.length;
    els.resultText.textContent = state.category === "all"
      ? copy[lang].countAll
      : copy[lang].countCategory(labelOf(activeCategory));

    if (visibleList.length === 0) {
      els.projectGrid.innerHTML = `<div class="empty-state">${escapeHtml(copy[lang].empty)}</div>`;
      els.loadMore.hidden = true;
      return;
    }

    els.projectGrid.innerHTML = visibleList
      .map((project) => {
        const category = primaryCategory(project);
        const categoryLabel = labelOf(category);
        const image = projectImage(project, category);
        const deliverables = inferDeliverables(project).slice(0, 3);
        const chips = [categoryLabel, inferLevel(project), ...deliverables]
          .slice(0, 5)
          .map((chip) => `<span class="chip">${escapeHtml(chip)}</span>`)
          .join("");

        return `
          <article class="project-card">
            <div class="project-media">
              <img src="${escapeHtml(image)}" alt="${escapeHtml(copy[lang].projectAlt(project.name))}" loading="lazy">
              <span class="project-id">P${String(project.id).padStart(3, "0")}</span>
            </div>
            <div class="project-body">
              <h3>${escapeHtml(project.name)}</h3>
              <p class="project-desc">${escapeHtml(project.description)}</p>
              <div class="chip-row">${chips}</div>
              <p class="tech-line">${escapeHtml(project.tech)}</p>
              <div class="project-actions">
                <span class="access-badge">${escapeHtml(project.access)}</span>
                <button class="details-button" type="button" data-project-id="${project.id}">${escapeHtml(copy[lang].details)}</button>
              </div>
            </div>
          </article>
        `;
      })
      .join("");

    els.loadMore.hidden = state.visible >= list.length;
  }

  function renderStats() {
    if (els.statTotal) {
      els.statTotal.textContent = projects.length;
    }
  }

  function render() {
    renderCategories();
    renderProjects();
    renderStats();
  }

  function openProject(projectId) {
    const project = projects.find((item) => item.id === Number(projectId));
    if (!project) return;

    const category = primaryCategory(project);
    const categoryLabel = labelOf(category);
    const image = projectImage(project, category);
    const deliverables = inferDeliverables(project);
    const items = techItems(project);
    const links = resourceLinks(project);
    const subject = `P${String(project.id).padStart(3, "0")} ${project.name}`;

    els.dialogContent.innerHTML = `
      <div class="dialog-inner">
        <div class="dialog-hero">
          <img src="${escapeHtml(image)}" alt="${escapeHtml(copy[lang].dialogImageAlt(project.name))}">
        </div>
        <div class="dialog-title-row">
          <div class="chip-row">
            <span class="chip">P${String(project.id).padStart(3, "0")}</span>
            <span class="chip">${escapeHtml(categoryLabel)}</span>
            <span class="chip">${escapeHtml(inferLevel(project))}</span>
            <span class="chip">${escapeHtml(project.access)}</span>
          </div>
          <h2 id="dialogTitle">${escapeHtml(project.name)}</h2>
        </div>
        <div class="dialog-section">
          <h3>${escapeHtml(copy[lang].functionTitle)}</h3>
          <p>${escapeHtml(project.description)}</p>
        </div>
        <div class="dialog-section">
          <h3>${escapeHtml(copy[lang].techTitle)}</h3>
          <ul class="tech-list">
            ${items.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}
          </ul>
        </div>
        <div class="dialog-section">
          <h3>${escapeHtml(copy[lang].materialsTitle)}</h3>
          <div class="chip-row">
            ${deliverables.map((item) => `<span class="chip">${escapeHtml(item)}</span>`).join("")}
          </div>
        </div>
        ${links.length > 0 ? `
          <div class="dialog-section">
            <h3>${escapeHtml(copy[lang].resourceTitle)}</h3>
            <div class="resource-links">
              ${links.map((item) => `<a href="${escapeHtml(item.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(item.label)}</a>`).join("")}
            </div>
          </div>
        ` : ""}
        <div class="dialog-section">
          <h3>${escapeHtml(copy[lang].accessTitle)}</h3>
          <p>${escapeHtml(copy[lang].accessText(subject))}</p>
        </div>
      </div>
    `;

    if (typeof els.dialog.showModal === "function") {
      els.dialog.showModal();
    } else {
      els.dialog.setAttribute("open", "");
    }
  }

  function closeDialog() {
    if (typeof els.dialog.close === "function") {
      els.dialog.close();
    } else {
      els.dialog.removeAttribute("open");
    }
  }

  async function loadProjects() {
    if (!window.fetch || window.location.protocol === "file:") {
      return;
    }

    try {
      const response = await fetch("/api/projects", { headers: { Accept: "application/json" } });
      if (!response.ok) return;
      const data = await response.json();
      if (Array.isArray(data.projects)) {
        projects = data.projects;
      }
    } catch (error) {
      // Keep the static data fallback when the backend is not running.
    }
  }

  els.categoryGrid.addEventListener("click", (event) => {
    const button = event.target.closest("[data-category]");
    if (!button) return;
    state.category = button.dataset.category;
    state.visible = 24;
    render();
  });

  els.projectGrid.addEventListener("click", (event) => {
    const button = event.target.closest("[data-project-id]");
    if (!button) return;
    openProject(button.dataset.projectId);
  });

  els.search.addEventListener("input", (event) => {
    state.query = event.target.value;
    state.visible = 24;
    renderProjects();
  });

  els.sort.addEventListener("change", (event) => {
    state.sort = event.target.value;
    state.visible = 24;
    renderProjects();
  });

  els.loadMore.addEventListener("click", () => {
    state.visible += 24;
    renderProjects();
  });

  document.addEventListener("click", (event) => {
    if (event.target.matches("[data-close-dialog]")) {
      closeDialog();
    }
  });

  els.dialog.addEventListener("click", (event) => {
    const rect = els.dialog.getBoundingClientRect();
    const clickedBackdrop =
      event.clientX < rect.left ||
      event.clientX > rect.right ||
      event.clientY < rect.top ||
      event.clientY > rect.bottom;
    if (clickedBackdrop) closeDialog();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && els.dialog.open) {
      closeDialog();
    }
  });

  loadProjects().then(render);
})();
