"""empty message

Revision ID: a77c604130a8
Revises: 304341d2ac22
Create Date: 2022-06-03 11:43:15.668882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a77c604130a8'
down_revision = '304341d2ac22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('show', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('show', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_foreign_key(None, 'show', 'venue', ['venue_id'], ['id'])
    op.create_foreign_key(None, 'show', 'artist', ['artist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'show', type_='foreignkey')
    op.drop_constraint(None, 'show', type_='foreignkey')
    op.alter_column('show', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('show', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###