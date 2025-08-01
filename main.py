def define_env(env):
    def version_badge(version, label="Added", icon="tag-outline", href=None, tooltip="Minimum version"):
        icon_markup = f":material-{icon}:"
        version_link = href or f"#v{version}"

        return f'''
<span class="mdx-badge" title="{tooltip}">
  <span class="mdx-version-box">
    <span class="mdx-badge__icon">{icon_markup}</span>
    <span class="mdx-badge__text">
      <a href="{version_link}">{label} {version}</a>
    </span>
  </span>
</span>
        '''
    env.macro(version_badge)
